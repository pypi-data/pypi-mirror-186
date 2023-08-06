"""Contains module logic."""
import concurrent.futures
import pickle
import sys
from datetime import datetime, timedelta
from multiprocessing import cpu_count

import numpy as np
import pandas as pd
import pgzip
import scipy.stats as stats
from sklearn.ensemble import IsolationForest
from sklearn.metrics import (
    average_precision_score,
    cohen_kappa_score,
    mean_absolute_error,
    precision_recall_curve,
)
from tqdm import tqdm

from .ft import FeatureTransformer
from .io import fetch_from_bucket, insert_logs, logger, upload_to_bucket
from .utils import apply_function, check_memory_consumption, process_col_status


def parallelize_clean_data(params, data):
    """Parallelized clean data.

    - data: Pass the data frame.
    - parallelization: Boolean if parallelization is required or not.
    """
    # If parallelization is applied
    if params["parallelize"]:
        result = []
        num_cores = cpu_count()
        with tqdm(total=data.shape[1]) as pbar:
            # Push all function calls with ThreadPoolexecutor that runs only 8 in parallel
            with concurrent.futures.ThreadPoolExecutor(
                max_workers=num_cores
            ) as executor:
                features = {
                    executor.submit(
                        process_col_status,
                        data[col].name,
                        data[col],
                        data[col].dtype,
                    )
                    for col in data.columns
                }
                for res in concurrent.futures.as_completed(features):
                    result.append(res.result())
                    pbar.update()

    else:
        # Clean data without parallelization
        result = []
        for i in tqdm(range(data.shape[1])):
            result += [
                process_col_status(
                    data.iloc[:, i].name,
                    data.iloc[:, i],
                    data.iloc[:, i].dtype,
                )
            ]

    # Merge the results
    cat_list = {i["name"]: i["type_inferred"] for i in result}

    usable_fields = [
        "id",
        "bool",
        "date",
        "datetime",
        "unix_timestamp",
        "timestamp",
        "numerical",
        "categorical",
    ]
    usable_cols = [k for k, v in cat_list.items() if v in usable_fields]
    df_clean = data.loc[:, usable_cols]
    cat_list = {k: v for k, v in cat_list.items() if v in usable_fields}

    return df_clean, cat_list


def filter_data(params, data, cat_list):
    """Filter categorical columns using Cramér's V association.

    https://en.wikipedia.org/wiki/Cramér's_V
    """
    # Init results
    categoricals = [cat["name"] for cat in cat_list if cat["type"] == "categorical"]
    col_remove = []

    # Run along pairs of categorical columns
    for cat_idx_i, cat_name_i in enumerate(categoricals):
        for cat_idx_j, cat_name_j in enumerate(
            categoricals[cat_idx_i + 1 :]  # noqa E203
        ):

            # Save time: process columns only if not removed yet
            if cat_name_i not in col_remove and cat_name_j not in col_remove:

                # Extract data
                paired_data = data[[cat_name_i, cat_name_j]].dropna()

                # If the df contains sth
                if paired_data.shape[0]:

                    # Compute contingency table
                    cat_contingency = pd.crosstab(
                        paired_data[cat_name_i], paired_data[cat_name_j]
                    )

                    # Chi-squared test statistic
                    chi_sq = stats.chi2_contingency(cat_contingency, correction=False)[
                        0
                    ]

                    # Try to remove column categories, only if the feature has multiple ones
                    if cat_contingency.shape[1] > 1:
                        # Compute Cramer's V for the pair of categoricals
                        cramer_v = np.sqrt(
                            (chi_sq / paired_data.shape[0])
                            / (cat_contingency.shape[1] - 1)
                        )

                        # Store columns to be removed
                        if cramer_v > params["abs_corr_collinearity"]:
                            col_remove.append(cat_name_j)

    cat_valid = [cat for cat in categoricals if cat not in col_remove]

    return cat_valid


def data_transformation(params, data):
    """Clean data and perform basic feature extraction."""
    if not params["train_mode"]:
        return data, None

    if data.shape[1] <= 1:
        msg = "Too few columns"
        logger.error(msg)
        if not params["dry_run"]:
            insert_logs(params, msg)
        sys.exit(-1)

    msg = "Cleaning data..."
    logger.info(msg)
    if not params["dry_run"]:
        insert_logs(params, msg)
    cat_processed = apply_function(process_col_status, params, data, axis=1)
    dtype_dict = {i["name"]: i["type_inferred"] for i in cat_processed}

    # Filter out only useful type fields
    usable_cols = [k for k, v in dtype_dict.items() if v in params["types_processed"]]
    df_clean = data.loc[:, usable_cols]
    dtype_dict = {k: v for k, v in dtype_dict.items() if v in params["types_processed"]}

    # msg = "Filtering data..."
    # logger.info(msg)
    # insert_logs(params, msg)
    # cat_valid = filter_data(params, data, cat_list)

    # logger.info(msg)
    # insert_logs(params, msg)
    # data = feat_extraction(params, data, cat_list, cat_valid)

    return df_clean, dtype_dict


# def feat_extraction(params, data, col_list, cat_valid):
#     """Perform feature extraction depending on data type."""
#     # Init results
#     cols_to_add_bool = []
#     cols_to_add_no_bool = []
#     cols_to_remove = []
#
#     # Run across features
#     for col in tqdm(col_list, total=len(col_list)):
#
#         # If column is a datetime, extract relevant features
#         if col["type"] == "datetime":
#
#             # Create dataframe with new datetime features
#             dt_split = extract_date_features(data[col["name"]]).astype(int)
#
#             # Add dataframe to list
#             cols_to_add_no_bool.append(dt_split)
#
#         # Otherwise, a numeric column might contain NAs
#         elif col["type"] == "numeric":
#             # Create dataframe with new numeric features
#             col_is_na, col_no_na = extract_num_features(params, data[col["name"]])
#
#             # Add dataframes to lists
#             # cols_to_add_bool.append(col_is_na)
#             cols_to_add_no_bool.append(col_no_na)
#
#             # Add feature to list of removable ones
#             cols_to_remove.append(col["name"])
#
#         # Otherwise, a categorical column might or not be valid
#         elif col["type"] == "categorical":
#
#             # Valid categorical columns are one-hot encoded into dummies
#             if col["name"] in cat_valid:
#
#                 # Create dataframe with one-hot encoded features
#                 data_dummies = pd.get_dummies(data[col["name"]], prefix=col["name"])
#
#                 # Add dataframe to list
#                 cols_to_add_bool.append(data_dummies)
#
#             # Add feature to list of removable ones
#             cols_to_remove.append(col["name"])
#
#     # Drop the columns to be removed
#     data.drop(columns=cols_to_remove, axis=1, inplace=True)
#
#     # Define column names and decide if boolean
#     col_bool = [col for df in cols_to_add_bool for col in df.columns]
#     col_no_bool = [col for df in cols_to_add_no_bool for col in df.columns]
#
#     # Update dataframe with columns_to_add
#     df_to_add_bool = pd.DataFrame(np.hstack(cols_to_add_bool), columns=col_bool)
#     df_to_add_no_bool = pd.DataFrame(
#         np.hstack(cols_to_add_no_bool), columns=col_no_bool
#     ).astype("float32")
#
#     # Join dataframes
#     data = data.join(df_to_add_no_bool).join(df_to_add_bool)
#
#     return data


def train_val_split(params, data, df, labels=None):
    """Split randomly train and validation sets + assign targets.

    - data: Data dictionary.
    -df: Data frame to split train and validation data.
    """
    # Initialise the splitting index
    split_index = params["id_field"]
    # Split data randomly between train and validation
    data["id_all"] = df[split_index].drop_duplicates().sort_values()
    today = datetime.utcnow()

    if params["val_split_timeseries"]:
        logger.info("Time based separation of training and validation")

        if "validation_test_split" in params and params["validation_test_split"]:
            logger.info("Separating train-val-validation_test ids")

            date_time_diff = today - timedelta(days=params["initial_days"])

            train_split = date_time_diff + timedelta(days=params["train_days"])
            val_split = pd.to_datetime(train_split) + timedelta(days=params["val_days"])

            train_split_date = pd.to_datetime(
                train_split, utc=True, infer_datetime_format=True
            )

            val_split_date = pd.to_datetime(
                val_split, utc=True, infer_datetime_format=True
            )

            ind_test = (
                df[["shipment_id", "upload_date", "service_completion_estimated_date"]]
                .sort_values("upload_date")
                .groupby("shipment_id")
                .last()["service_completion_estimated_date"]
                .between(train_split_date, val_split_date)
            )

            data["id_val"] = ind_test[ind_test].index

        else:
            train_split = datetime.today() - timedelta(
                days=params["val_days"]
            )  # 150 days

            train_split_date = pd.to_datetime(
                train_split, utc=True, infer_datetime_format=True
            )

        ind_train = (
            df[["shipment_id", "upload_date", "service_completion_estimated_date"]]
            .sort_values("upload_date")
            .groupby("shipment_id")
            .last()["service_completion_estimated_date"]
            < train_split_date
        )

        data["id_train"] = ind_train[ind_train].index

    else:
        logger.info("Random separation of training and validation")
        logger.info("Separating ids")
        data["id_train"] = list(
            data["id_all"]
            .sample(
                frac=params["train_test_split"], random_state=params["random_state"]
            )
            .values
        )

    if "validation_test_split" in params and params["validation_test_split"]:

        data["id_test"] = list(
            set(data["id_all"]) - set(data["id_train"]) - set(data["id_val"])
        )
        segments = ["train", "val", "test"]
    else:
        data["id_val"] = list(set(data["id_all"]) - set(data["id_train"]))
        segments = ["train", "val"]

    # Loop over train and validation segments
    for segment in segments:
        logger.info(f"Extracting {segment} data")
        # Select the index of a selected shipments of a segment
        idx = df[split_index].isin(data[f"id_{segment}"])

        # Assign segment data
        data[f"df_{segment}"] = df[idx].reset_index(drop=True)

        df = df[~idx]

        if labels is not None:
            logger.info("Merging labels")
            # Get shipment_ids
            data[f"id_{segment}"] = pd.DataFrame(data[f"df_{segment}"][split_index])

    return data


def apply_if_train(params, data, cat_list):
    """Apply Isolation Forest outlier detection on training data."""
    msg = "Filtering outliers with IsolationForest..."
    logger.info(msg)

    # Extract numeric features and drop null columns
    df_numeric = data[
        [
            var
            for var in cat_list
            if cat_list[var] in ["bool", "numerical"] and var in data.columns
        ]
    ]
    df_numeric = (
        df_numeric.astype(np.float32)
        .fillna(df_numeric.median())
        .dropna(axis=1, how="all")
    )

    # Make a run of IsolationForest with auto best-fit contamination
    if_params = params["if_params"]
    contamination = (
        if_params["contamination"] if "contamination" in if_params else "auto"
    )

    if_model = IsolationForest(
        n_estimators=if_params["n_estimators"],
        max_samples=if_params["sr_isolation"],
        max_features=1.0,
        random_state=params["random_state"],
        contamination=contamination,
        n_jobs=-1,
    )
    if_model.fit(df_numeric)
    if_pred = if_model.predict(df_numeric)

    contamination = ((1 - if_pred) / 2).mean()
    logger.info(f"The current run has contamination = {contamination:.4f}")

    # Perform IsolationForest outlier detection
    data = data[if_pred == 1]

    return data


def data_etl(params, df, labels=None, **kwargs):
    """Acquire data / etl pipeline."""
    check_memory_consumption(params, df)

    # If there are ids to ignore:
    # In some projects, we might have incomplete labels as they are filled from other stakeholders.
    # This is a parameter to incorporate that behavior.
    if "id_ignore" in kwargs:
        pass

    # Clean data
    logger.info("Performing etl...")
    df, type_dict = data_transformation(params, df)
    check_memory_consumption(params, df)

    # Store results
    data = {"df_n_vars": df.shape[1]}

    if params["train_mode"]:
        # Create reference data dictionary
        data = train_val_split(params, data, df, labels)
        # during train mode, infer data schema. Test mode inherits schema from associate training session.
        params["type_dict"] = type_dict

        # Perform IsolationForest on training data
        if params["isolation"]:
            data["df_train"] = apply_if_train(
                params, data["df_train"], params["type_dict"]
            )
            check_memory_consumption(params, data["df_train"])
            data["id_train"] = data["id_train"].loc[data["df_train"].index]

            # Reset indexes since if breaks categorical encoding
            data["df_train"] = data["df_train"].reset_index(drop=True)
            data["id_train"] = data["id_train"].reset_index(drop=True)

        # Upload train and val data (both feature and labels) to bucket folder
        if not params["dry_run"]:
            # Pickle train and val data (both features and labels)
            logger.info("Pickling data...")
            num_cores = cpu_count()
            with pgzip.open(
                params["path_train_data_file"],
                "wb",
                blocksize=2**22,
                compresslevel=4,
                thread=num_cores,
            ) as f:
                pickle.dump(data, f)

            msg = "Uploading the data to bucket..."
            logger.info(msg)
            insert_logs(params, msg)
            upload_to_bucket(
                params,
                params["path_train_data_file"],
                params["train_data_file"],
                bucket_folder="train_data",
            )

        # Transform features via Feature Transformer
        ft_fixed_columns = [params["id_field"], params["datetime_field"]]
        if "data_normalization_field" in params and params["data_normalization_field"]:
            ft_fixed_columns += [params["data_normalization_field"]]

        ft = FeatureTransformer(
            fixed_columns=ft_fixed_columns,
            parallelization=params["parallelize"],
            ft_encoding=params["ft_encoding"],
        )

        if "validation_test_split" in params and params["validation_test_split"]:
            segments = ["train", "val", "test"]
        else:
            segments = ["train", "val"]
        for segment in segments:
            # Do label gathering first since you need it for LDA
            data[f"label_{segment}"] = (
                data[f"id_{segment}"]
                .merge(labels, on=params["id_field"], how="left")
                .set_index(params["id_field"])
                .fillna(0)
            )

            if (
                "data_normalization_field" in params
                and params["data_normalization_field"]
            ):
                data[f"norm_{segment}"] = data[f"df_{segment}"][
                    [params["id_field"], params["data_normalization_field"]]
                ].set_index(params["id_field"])
                data[f"norm_{segment}"] = data[f"norm_{segment}"][
                    ~data[f"norm_{segment}"].index.duplicated(keep="first")
                ]

            if segment == "train":
                logger.info("Feature extraction... Fitting")
                ft.fit(
                    params, data["df_train"], data["label_train"], params["type_dict"]
                )

            data[f"df_{segment}"] = ft.transform(params, data[f"df_{segment}"])

            # Do it again since Feature Transformer groups shipments
            data[f"label_{segment}"] = (
                pd.DataFrame(data[f"df_{segment}"][params["id_field"]])
                .merge(labels, on=params["id_field"], how="left")
                .set_index(params["id_field"])
                .fillna(0)
            )

            data[f"id_{segment}"] = pd.DataFrame(
                data[f"df_{segment}"][params["id_field"]]
            )

            data[f"df_{segment}"] = (
                data[f"df_{segment}"]
                .drop(
                    [params["id_field"], params["datetime_field"]],
                    axis=1,
                    errors="ignore",
                )
                .fillna(params["na_replace_val"])
            )
        check_memory_consumption(params, data["df_train"])

        data["data_num_input"] = data["df_train"].shape[1]
        data["data_num_output"] = params["data_n_output"]

        if not params["dry_run"]:
            num_cores = cpu_count()
            # Pickle FeatureTransformer since we will need it for test
            logger.info("Pickling FeatureTransformer...")
            pickle.dump(
                ft,
                pgzip.open(
                    params["path_ft_file"], "wb", thread=num_cores, blocksize=2**22
                ),
            )

    else:
        # Pickle test data feature
        num_cores = cpu_count()
        pickle.dump(
            df,
            pgzip.open(
                params["path_test_data_file"],
                "wb",
                thread=num_cores,
                blocksize=2**22,
            ),
        )

        # upload test data features to bucket folder
        if not params["dry_run"]:
            msg = "Uploading the test data to bucket..."
            logger.info(msg)
            insert_logs(params, msg)
            upload_to_bucket(
                params,
                params["path_test_data_file"],
                params["test_data_file"],
                bucket_folder="test_data",
            )

        df = df.drop("label", axis=1, errors="ignore")
        # Loading FeatureTransformer object
        ft = fetch_from_bucket(params, to_download="ft")["ft"]

        # Transform test data
        msg = "Feature transformation of test data"
        logger.info(msg)
        insert_logs(params, msg)
        data["df_test"] = ft.transform(params, df)
        data["id_test"] = data["df_test"][params["id_field"]]
        data["df_test"] = (
            data["df_test"]
            .drop(
                [params["id_field"], params["datetime_field"]], axis=1, errors="ignore"
            )
            .fillna(params["na_replace_val"])
        )
        data["data_num_input"] = data["df_test"].shape[1]
        data["data_num_output"] = params["data_n_output"]

    return data


def kappa_analysis(params, data):
    """Do kappa analysis for classification tasks and returns optimal threshold."""
    logger.info("Kappa analysis for optimal threshold finding...")
    # Define threshold ranges
    x = list(np.arange(0, 1, 0.01))

    # Define training and prediction values
    tr = data["label_val"].values.flatten()
    pr = np.array(data["pred_val"]).flatten()

    # Kappa analysis by simple threshold
    k = []
    for t in tqdm(np.arange(0, 1, 0.01)):
        k += [cohen_kappa_score(tr, (pr >= t))]

    best_x = x[np.argmax(k)]
    best_kappa = np.max(k)
    pred_ratio = (pr >= best_x).mean()

    results = {
        "x": x,
        "k": k,
        "best_x": best_x,
        "best_kappa": best_kappa,
        "pred_ratio": pred_ratio,
    }

    logger.info(f"Best threshold: {best_x}")
    logger.info(f"Best Kappa value: {best_kappa}")
    logger.info(f"Expected positive prediction ratio: {pred_ratio}")
    logger.info("Kappa analysis is done.")

    return results


def calculate_mean_average_precision(params, data):
    """Store mean average precision per category. Works for multiple categories."""
    results = {}
    if params["data_n_output"] > 1:
        results = {"mAp_per_category": {}, "pr_per_category": {}, "rc_per_category": {}}

        # Plot curves per category of the labels
        for label_cat in data["label_val"].columns:
            # Compute precision, recall, and mAp score
            results["mAp"] = average_precision_score(
                data["label_val"][label_cat], data["pred_val"][label_cat]
            )
            results["pr"], results["rc"], _ = precision_recall_curve(
                data["label_val"][label_cat], data["pred_val"][label_cat]
            )

            # Store the results
            results["mAp_per_category"][label_cat] = np.round(results["mAp"], 4)
            results["pr_per_category"][label_cat] = list(np.round(results["pr"], 4))
            results["rc_per_category"][label_cat] = list(np.round(results["rc"], 4))

    # Calculate P/R curve for all categories
    data["total_label"] = data["label_val"].sum(axis=1) > 0
    data["total_pred"] = data["pred_val"].sum(axis=1)

    results["mAp"] = average_precision_score(data["total_label"], data["total_pred"])
    results["pr"], results["rc"], _ = precision_recall_curve(
        data["total_label"], data["total_pred"]
    )

    # Convert to list from numpy array. Else, insert_to_metrics will throw an error.
    results["mAp"] = np.round(results["mAp"], 4)
    results["pr"] = list(np.round(results["pr"], 4))
    results["rc"] = list(np.round(results["rc"], 4))

    # Calculate the overall results if outputs are > 1
    if params["data_n_output"] > 1:
        # Store the average score of all categories
        results["mAp_per_category"]["Overall"] = np.round(results["mAp"], 4)
        results["pr_per_category"]["Overall"] = list(np.round(results["pr"], 4))
        results["rc_per_category"]["Overall"] = list(np.round(results["rc"], 4))

    # Insert the score to logs
    msg = f"Average Precision: {results['mAp']:.4f}"
    logger.info(msg)
    if not params["dry_run"]:
        insert_logs(params, msg)

    return results


def calculate_mean_absolute_error(params, data):
    """Calculate mean absolute error for regression tasks. Also works on normalized data."""
    # Denormalize labels (if required)
    if "data_normalization_field" in params and params["data_normalization_field"]:
        # de-normalize over TEUs
        data[f"pred_val_denormalized"] = pd.DataFrame(
            data[f"norm_val"].join(data["pred_val"]).prod(axis=1), columns=["pred"]
        )
        data["label_val_denormalized"] = pd.DataFrame(
            data[f"norm_val"].join(data["label_val"]).prod(axis=1), columns=["label"]
        )

    else:
        data[f"pred_val_denormalized"] = data["pred_val"]
        data["label_val_denormalized"] = data["label_val"]

    # compute Mean Absolute Error of predictions
    results = {}
    for norm in ["", "_denormalized"]:
        results[f"mae{norm}"] = mean_absolute_error(
            data[f"pred_val{norm}"]["pred"], data[f"label_val{norm}"]["label"]
        ).astype(float)
        logger.info(
            f"Average MAE{norm}: {results[f'mae{norm}']:.2f} {params['data_pred_unit']}"
        )

    return results
