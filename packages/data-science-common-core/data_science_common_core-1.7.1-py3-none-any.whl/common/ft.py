"""Feature Extraction and Transformation functionalities."""
from collections import OrderedDict

import numpy as np
import pandas as pd
from sklearn.covariance import OAS
from sklearn.decomposition import NMF, PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, StandardScaler
from tqdm import tqdm

from .io import insert_logs, logger
from .utils import apply_function


def extract_date_features(ds, ds_datetime_field, date_time=True, time_delta=True):
    """Extract date features from a column.

    - ds: data series of datetime/date type to extract features.
    - date_time: Boolean input.
        if date_time=True: Extract all the features
        if date_time=False: Extract only day and dayofweek features.
    - time_delta: Boolean input.
        if time_delta=True: Extract time delta features between column and datetime column (upload_date)
        if time_delta=False: Do not extract time delta features
    """
    # Extract day and dayofweek
    res = [
        ds.dt.day,
        ds.dt.dayofweek,
    ]

    # Column names
    res_columns = [
        f"{ds.name}_days",
        f"{ds.name}_hours",
    ]

    # Extract all the features if the condition is true
    if date_time:
        res += [
            ds.dt.year,
            ds.dt.month,
            ds.dt.hour,
            ds.dt.minute,
            ds.dt.dayofyear,
            ds.dt.isocalendar().week,
            ds.dt.days_in_month,
        ]

        res_columns += [
            f"{ds.name}_year",
            f"{ds.name}_month",
            f"{ds.name}_hour",
            f"{ds.name}_minute",
            f"{ds.name}_day_of_year",
            f"{ds.name}_week_of_year",
            f"{ds.name}_days_in_month",
        ]

    # Extract all the features if the condition is true
    if time_delta:
        ds_td = ds.dt.tz_localize(None) - ds_datetime_field.dt.tz_localize(None)
        res += [
            ds_td.dt.days,
            ds_td.dt.seconds // 3600,
        ]

        res_columns += [
            f"{ds.name}_time_delta_days",
            f"{ds.name}_time_delta_hours",
        ]

    res = pd.concat(res, axis=1)
    res.columns = res_columns

    return res.astype(np.float32)


def extract_num_features(params, ds):
    """Extract and replace NaNs from numeric feature."""
    # Check where NAs are
    find_na = ds.isna()
    col_is_na = pd.DataFrame(find_na.astype("uint8")).rename(
        columns={f"{ds.name}": f"{ds.name}_isna"}
    )

    # Replace NA values with default constant
    col_no_na = ds.copy()
    col_no_na[find_na] = np.float32(params["NA_replace_val"])
    col_no_na = pd.DataFrame(col_no_na)

    return col_is_na, col_no_na


class FeatureTransformer:
    """FeatureTransformer class with ordinal encoder."""

    def __init__(
        self,
        fixed_columns=[],
        json_columns=[],
        category_cross=False,
        detect_gap=5,
        verbose=0,
        parallelization=False,
        ft_encoding="lda",
    ):
        """Class initializer."""
        self.fixed_columns = fixed_columns
        self.json_columns = json_columns
        self.category_cross = category_cross
        self.detect_gap = detect_gap
        self.verbose = verbose
        self.columns = OrderedDict()
        self.parallelization = parallelization
        self.ft_encoding = ft_encoding
        self.enc = []
        self.dim_red = []

    def process_column_types(self, params, type_dict):
        """Process type_dict and create ordered col_names and col_types."""
        # Filter the fixed columns and wanted columns
        dict_dtypes = OrderedDict()
        for k, v in type_dict.items():
            if v in params["types_processed"] and k not in self.fixed_columns:
                dict_dtypes[k] = v
        self.col_names = [k for k, _ in dict_dtypes.items()]
        self.col_types = [v for _, v in dict_dtypes.items()]

    def _fit_one_column(self, params, ds, label_enc, i):
        """Apply fix operation on one column."""
        col_type = self.col_types[i]

        if col_type == "categorical":
            if self.ft_encoding == "pca":
                enc = OneHotEncoder(
                    sparse=False,
                    handle_unknown="infrequent_if_exist",
                    max_categories=params["max_ohe_categories"],
                )
                dim_red = PCA(
                    n_components=params["pca_variance"], whiten=params["pca_whitening"]
                )

                temp = enc.fit_transform(pd.DataFrame(ds))
                dim_red.fit(temp)
            elif self.ft_encoding == "lda":
                enc = OneHotEncoder(
                    sparse=False,
                    handle_unknown="infrequent_if_exist",
                    max_categories=params["max_ohe_categories"],
                )
                oa = OAS(store_precision=False, assume_centered=False)
                dim_red = LDA(
                    solver="eigen",
                    covariance_estimator=oa,
                    n_components=params["lda_n_components"],
                )

                temp = enc.fit_transform(pd.DataFrame(ds))
                dim_red.fit(temp, label_enc)
            elif self.ft_encoding == "nmf":
                enc = OneHotEncoder(
                    sparse=True,
                    handle_unknown="infrequent_if_exist",
                    max_categories=params["max_ohe_categories"],
                    min_frequency=params["min_frequency"],
                )
                dim_red = NMF(n_components=params["nmf_n_components"])

                temp = enc.fit_transform(pd.DataFrame(ds))
                dim_red.fit(temp)
            else:
                # Catboost needs categorical variables of type str/int, not float
                enc = OrdinalEncoder(
                    handle_unknown="use_encoded_value", unknown_value=-1, dtype=np.int16
                )
                dim_red = enc

                enc.fit(pd.DataFrame(ds))

            return i, (enc, dim_red)

        elif col_type == "numerical":
            if params["scaling"]:
                sc = StandardScaler()
                sc.fit(pd.DataFrame(ds))

                return i, (sc, None)
            else:
                return i, (None, None)

        else:
            return i, (None, None)

    def fit(self, params, df, label, col_dtypes):
        """Fit transformer with data."""
        """Get processable column names and types."""
        self.process_column_types(params, col_dtypes)

        # cat_cols = [c for c,t in zip(self.col_names, self.col_types) if t == 'categorical']
        #
        # # Perform feature crossing between categorical columns
        # self.combined_cols = []
        # if self.category_cross:
        #     msg = f"Feature Crossing between {len(cat_cols)} columns"
        #     logger.info(msg)
        #     insert_logs(params, msg)
        #     for i1 in tqdm(range(len(cat_cols) - 1)):
        #         for i2 in range(i1 + 1, len(cat_cols)):
        #             c1, c2 = cat_cols[i1], cat_cols[i2]
        #             new_col = f"{c1}___{c2}"
        #             df.loc[:, new_col] = df[c1].astype(str) + "___" + df[c2].astype(str)
        #             self.combined_cols += [new_col]
        # self.cat_cols += self.combined_cols

        # Label Encoding for LDA
        if params["prediction_type"] == "classification":
            oe = OrdinalEncoder()
            label_enc = label.astype(int).astype(str).values.sum(axis=1)
            label_enc = oe.fit_transform(label_enc.reshape(-1, 1)).flatten()
        else:
            bins = np.histogram(label, params["regression_bins"])[1]
            label_enc = np.digitize(label, bins)

        df_wanted = df.loc[:, self.col_names]
        res = apply_function(self._fit_one_column, params, df_wanted, label_enc, axis=1)
        self.enc = [i[0] for i in res]
        self.dim_red = [i[1] for i in res]

        return self

    # Extract features from numeric and datetime columns
    def _process_one_column(self, params, col_data, ds_datetime_field, i):
        ret = pd.DataFrame(index=col_data.index)
        if len(col_data) < 2:
            return i, ret

        col_type = self.col_types[i]
        if col_type in ["bool", "numerical"]:
            ret = pd.DataFrame(
                pd.to_numeric(col_data, errors="coerce", downcast="float")
                .astype(np.float32)
                .fillna(params["na_replace_val"])
            )
            if col_type == "numerical" and self.enc[i]:
                ret = pd.DataFrame(
                    self.enc[i].transform(ret), columns=[self.col_names[i]]
                )

        elif col_type in ["date", "datetime", "timestamp"]:
            dt = pd.to_datetime(
                col_data, errors="coerce", utc=True, infer_datetime_format=True
            )
            ds_datetime_field = pd.to_datetime(
                ds_datetime_field, errors="coerce", utc=True, infer_datetime_format=True
            )
            ret = extract_date_features(dt, ds_datetime_field)
        elif col_type in ["unix_timestamp"]:
            dt = pd.to_datetime(
                col_data,
                errors="coerce",
                utc=True,
                infer_datetime_format=True,
                unit="s",
            )
            ret = extract_date_features(dt, ds_datetime_field)
        elif col_type == "categorical":
            ret = self.enc[i].transform(pd.DataFrame(col_data))

            if self.ft_encoding:
                ret = self.dim_red[i].transform(ret)
                n_cols = ret.shape[1]
                col_names = [
                    f"{self.col_names[i]}_{params['ft_encoding']}_{j}"
                    for j in range(n_cols)
                ]
                ret = pd.DataFrame(data=ret, columns=col_names)
            else:
                ret = pd.DataFrame(ret)
                ret.columns = [self.col_names[i]]

        return i, ret

    def _extract_feature_per_shipment_single(self, params, df):
        """Extract latest record and history statistics for each shipment."""
        # Generate statistics of history for each var and each shipment
        # Statistics to aggregate on numerical features
        num_operations = ["min", "mean", "max", "std"]
        num_features = [
            col
            for col in params["type_dict"]
            if params["type_dict"][col] == "numerical"
            and (col not in self.fixed_columns)
            and (col in df)
        ]
        # Statistics to aggregate on categorical features
        cat_operations = ["nunique"]
        cat_features = [
            col
            for col in params["type_dict"]
            if (params["type_dict"][col] == "categorical")
            and (col not in self.fixed_columns)
            and (col in df)
        ]
        # Statistics to aggregate on common features
        common_operations = ["first", "last"]

        df = df.sort_values([params["id_field"], params["datetime_field"]])
        df = df.drop(params["datetime_field"], axis=1)
        num_stats = df.groupby(params["id_field"])[num_features].agg(num_operations)
        if len(cat_features):
            cat_stats = df.groupby(params["id_field"])[cat_features].agg(cat_operations)
        # If ohe/pca/lda is performed, there are no categorical features
        else:
            cat_stats = pd.DataFrame()
        common_stats = df.groupby(params["id_field"]).agg(common_operations)

        per_shipment_df = pd.concat((num_stats, cat_stats, common_stats), axis=1)
        per_shipment_df.columns = ["_".join(i) for i in per_shipment_df.columns]
        params["processed_cat_features"] = [col + "_first" for col in cat_features] + [
            col + "_last" for col in cat_features
        ]

        return per_shipment_df

    # Transform only works on the same df format, considering same columns with same order
    def transform(self, params, df):
        """Transform input data with fitted transformer."""
        df_wanted = df.loc[:, self.col_names]

        # Feature transform on numeric and datetime columns
        logger.info("Extracting features per column.")
        result = apply_function(
            self._process_one_column,
            params,
            df_wanted,
            df[params["datetime_field"]],
            axis=1,
        )

        # for new_col in tqdm(self.combined_cols):
        #     c1, c2 = new_col.split("___")
        #     df.loc[:, new_col] = df[c1].astype(str) + "___" + df[c2].astype(str)

        # # Transform the ordinal encoders
        # df_cat = self.enc.transform(df[self.cat_cols])
        #
        # # Create categorical and numerical features into a dataframe
        # df_cat = pd.DataFrame(df_cat, columns=self.cat_cols, index=df.index)
        features = pd.concat(result, axis=1)

        msg = f"Feature shape before group by: {features.shape}"
        logger.info(msg)
        insert_logs(params, msg)

        features = features.set_index(df[params["id_field"]])
        # gr = features.groupby(params['id_field'])
        # gr = [(s_id, df_gr) for s_id, df_gr in gr]
        # gr = [i[1] for i in gr]
        # # Extract features per shipment
        # # logger.info("extracting features per shipment...")
        # ret = apply_function(
        #     self._extract_feature_per_shipment2,
        #     params,
        #     gr, axis=1
        # )
        # ret = pd.concat(ret, axis=0).reset_index()
        if (
            "extract_feature_per_shipment_single" in params
            and params["extract_feature_per_shipment_single"]
        ):
            # Extract a single feature per shipment
            features = pd.concat(
                [
                    df[[params["datetime_field"], params["id_field"]]],
                    features.reset_index(drop=True),
                ],
                axis=1,
            )
            ret = self._extract_feature_per_shipment_single(params, features)

        else:
            ret = features.copy()
        # ret = features

        # Concatenate fixed columns, numerical, datetime and categorical features
        # ret = pd.concat(
        #     [df.loc[:, df.columns.isin(self.fixed_columns)], *features], axis=1
        # )
        logger.info("...Finished extracting")
        logger.info(f"Data shape: {ret.shape[0]} rows, {ret.shape[1]} cols")

        return ret.reset_index()

    # transform_features works independent of the same df format such as same order in both training and testing
    # noqa E501
    def transform_features(self, params, df, feature_dtypes):
        """Minimal transformation to input data.

        - Date features: apply extract_date_features
        - Categorical features: fill missing values with "nan"
        - Extract feature per shipment based on history
        """
        # Filter out non_features
        feature_dtypes = {
            col: dtype
            for col, dtype in feature_dtypes.items()
            if col not in self.fixed_columns
        }

        # Select the datetime columns
        datetime_features = [
            col
            for col in feature_dtypes
            if feature_dtypes[col] in ["date", "datetime", "timestamp"]
        ]
        # Select the categorical columns
        cat_features = [
            col
            for col in feature_dtypes
            if feature_dtypes[col] in ["id", "categorical"]
        ]
        # Select the numerical columns
        num_features = [
            col
            for col in feature_dtypes
            if feature_dtypes[col] in ["bool", "numerical"]
        ]

        # Extract date features for columns of datetime type
        df_dt = []
        for c in tqdm(datetime_features):
            dt = pd.to_datetime(
                df[c], errors="coerce", utc=True, infer_datetime_format=True
            )
            ds_datetime_field = pd.to_datetime(
                df[params["datetime_field"]],
                errors="coerce",
                utc=True,
                infer_datetime_format=True,
            )
            df_dt += [
                extract_date_features(dt, ds_datetime_field).fillna(
                    params["na_replace_val"]
                )
            ]
        df_dt = pd.concat(df_dt, axis=1).set_index(df.index)

        # Fill categorical missing values with nan
        df[cat_features] = df[cat_features].fillna("nan")

        msg = f"Number of datetime features: {len(datetime_features)}"
        logger.info(msg)
        insert_logs(params, msg)

        msg = f"Number of numerical features: {len(num_features)}"
        logger.info(msg)
        insert_logs(params, msg)

        msg = f"Number of categorical features: {len(cat_features)}"
        logger.info(msg)
        insert_logs(params, msg)

        # Concat non-datetime features with newly transform datetime features
        ret = pd.concat([df.drop(columns=datetime_features), df_dt], axis=1)

        if (
            "extract_feature_per_shipment_single" in params
            and params["extract_feature_per_shipment_single"]
        ):
            # Extract features per shipment based on history
            # Reducing multiple rows for each shipment to one per shipment
            ret = self._extract_feature_per_shipment_single(ret)

        return ret

    # Fit and transform the featuretransformer
    def fit_transform(self, params, df):
        """Apply fit and transform to data."""
        self.fit(params, df)
        return self.transform(params, df)
