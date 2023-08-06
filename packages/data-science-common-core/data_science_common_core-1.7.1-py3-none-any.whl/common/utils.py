"""Utility functions for data science projects."""
import concurrent
import json
import random
import time
from multiprocessing import cpu_count

import pandas as pd
from tqdm import tqdm

from .io import insert_logs, logger


def ulid(hash_project):
    """Create unique identifier every time it runs, with respect to the hash_project."""
    hash_time = f"{int(time.time() * 1e3):012x}"
    hash_rand = f"{random.getrandbits(48):012x}"
    hash_all = hash_time + hash_project + hash_rand
    ulid = f"{hash_all[:8]}-{hash_all[8:12]}-{hash_all[12:16]}-{hash_all[16:20]}-{hash_all[20:32]}"
    return ulid


def check_memory_consumption(params, df):
    """Log RAM occupation of a df."""
    msg = f"Df memory occupation = {df.memory_usage(index=True).sum() / 1e6:.2f} Mb"
    logger.info(msg)
    insert_logs(params, msg)
    return


def json_to_series(text):
    """Explode json-like pandas record to full Series."""
    try:
        keys, values = zip(*[item for item in json.loads(text).items()])
        result = pd.Series(values, index=keys)
    except Exception:
        result = pd.Series()
    return result


def process_col_status(params, col_data, i):
    """Process a column and return its data type. Imported from DataMap."""
    # Initialize results
    col_info = {
        "name": col_data.name,
        "type_declared": col_data.dtype,
        "type_inferred": "NONE",
        "error_reason": None,
    }

    # Remove columns if constant or too dispersed
    col_type = "NONE"
    try:
        local_count = col_data[::10].nunique()
        # Column only has min_cardinality unique value, drop as its useless.
        min_cardinality = 1
        # LDA requires minimum cardinality than its number of components
        if params["ft_encoding"] == "lda":
            min_cardinality = params["lda_n_components"]
        if local_count < min_cardinality + 1:
            return i, col_info

    except TypeError as e:
        col_info["type_inferred"] = "ERROR"
        col_info[
            "error_reason"
        ] = f"Failed to count distinct in column sample, {str(e)}"
    else:
        # Log the kind of problem we find while cleaning the columns:
        # Empty column
        if not local_count:
            col_info["type_inferred"] = "ERROR"
            col_info["error_reason"] = "completely empty column sample"
        # Unique value in the column
        elif not (local_count - 1):
            col_info["type_inferred"] = "ERROR"
            col_info["error_reason"] = "constant value in column sample"
        else:
            # Extract column data type and ratio of unique values
            col_type = col_data.dtype.name

    if col_info["type_inferred"] != "id":

        # Check if column is a datetime, extract relevant features and join them
        if "datetime" in col_type:
            # Convert datetime type to make it uniform
            # Add to list of variable types
            col_info["type_inferred"] = "datetime"

        # Otherwise, the column is either a boolean, a numerical or a categorical
        else:

            # Try to check if it is proper BOOL
            is_bool = col_type == "bool"

            if is_bool:
                # Add to list of variable types
                col_info["type_inferred"] = "bool"

            else:
                # Assess it is a numerical
                try:
                    # Fill the None values with NaNs and downcast float
                    data_num = (
                        col_data.astype(float)
                        .fillna(value=params["na_replace_val"])
                        .astype(int)
                    )

                    # Given it is a numerical, assess whether it is a UNIX timestamp
                    # by checking the number of digits (11, 13, 15)
                    mi, ma = len(str(data_num.min())), len(str(data_num.max()))
                    # num_length = data_num.apply(lambda x: len(str(x).split(".0")[0]))
                    if mi == ma and ma in [
                        11,
                        13,
                        15,
                    ]:
                        # data_num.astype(int)
                        # Add to list of variable types
                        col_info["type_inferred"] = "unix_timestamp"
                    else:
                        # Add to list of variable types
                        col_info["type_inferred"] = "numerical"

                # Otherwise, it is some form of string
                except ValueError:

                    # Try to check if it is string-typed BOOL
                    is_bool = col_data.str.lower().isin(["true", "false"]).all()

                    if not is_bool:
                        # Try to check if it is JSON
                        try:
                            col_data.apply(json.loads)
                            # Add to list of variable types
                            col_info["type_inferred"] = "json"

                        # Treat it as a datetime string or actual categorical
                        except (json.decoder.JSONDecodeError, TypeError):

                            # Convert datetime type to make it uniform
                            try:
                                pd.to_datetime(col_data)
                                # Add to list of variable types
                                col_info["type_inferred"] = "timestamp"

                            # Actual categorical
                            except Exception:
                                # Add to list of variable types
                                col_info["type_inferred"] = "categorical"

                    else:
                        # Add to list of variable types
                        # col_info["type_inferred"] = "bool"
                        col_info["type_inferred"] = "categorical"

                # It might mistake the type
                except TypeError:

                    # Assess it is a date
                    try:
                        # Convert datetime type to make it uniform
                        pd.to_datetime(col_data)
                        # Add to list of variable types
                        col_info["type_inferred"] = "date"

                    # Treat it as mixed data type and log error
                    except Exception:
                        col_info["type_inferred"] = "ERROR"
                        col_info["error_reason"] = "mixed data type"
                        msg = f"{col_data.name}: {col_info['error_reason']}"
                        logger.warning(msg)

    return i, col_info


def apply_function(func, params, df, *args, axis=1):
    """Apply a function over a data either parallelized or not.

    func must take params as first parameter
    df must be data as second parameter
    *args are rest of all the args
    final argument of func is i which is the iterator you would like to go over
    axis is the axis of function applied.

    func must return i as index to keep order

    Returns a list for each element process on specified axis.
    """

    def axis_getter(df, i, axis):
        if axis == 0 or isinstance(df, list):
            return df[i]
        else:
            return df.iloc[:, i]

    # Feature transform on numeric and datetime columns with parallelization
    if params["parallelize"]:
        if axis == 1:
            if isinstance(df, list):
                total = len(df)
            else:
                total = df.shape[axis]
        else:
            total = len(df)
        result = [[]] * total

        num_cores = cpu_count()
        # Extra boost num_cores in bottlenecked functions
        if "boost_functions" in params and func.__name__ in params["boost_functions"]:
            coef = params["boost_functions"][func.__name__]
            num_cores = num_cores * coef

        with tqdm(total=total) as pbar:
            # Feature transform on numeric and datetime columns
            with concurrent.futures.ThreadPoolExecutor(
                max_workers=num_cores
            ) as executor:
                features = {
                    executor.submit(func, params, axis_getter(df, i, axis), *args, i)
                    for i in range(total)
                }
                for res in concurrent.futures.as_completed(features):
                    i, r = res.result()
                    result[i] = r
                    pbar.update()
    else:
        # Feature transform on numeric and datetime columns without parallelization
        # Take the second element as first element is i
        result = [
            func(params, axis_getter(df, i, axis), *args, i)[1]
            for i in range(df.shape[axis])
        ]
    return result
