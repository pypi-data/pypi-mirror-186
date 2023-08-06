"""Contains project setup parameters and initialization functions."""
import argparse
import json
import os
import sys

import toml
from dotenv import dotenv_values

# Parent repos are imported without .
from src.constants import project_parameters
from src.constants_debug import project_parameters_debug

from .io import insert_logs, logger
from .query import q_runs
from .utils import ulid


def parse_input(parent_parser=None):
    """Manage input parameters."""
    parser = (
        argparse.ArgumentParser(parents=[parent_parser], description="")
        if parent_parser
        else argparse.ArgumentParser(description="")
    )
    parser.add_argument(
        "--model_type",
        type=str,
        dest="model_type",
        required=False,
        help="Type of the model (either 'hgb', 'cat', 'lsq' or 'opt')",
    )
    parser.add_argument(
        "--model_id",
        type=str,
        dest="model_id",
        default="",
        required=False,
        help="ulid of the model",
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        dest="debug_mode",
        help="turn on debug mode",
    )
    parser.add_argument(
        "--train",
        action="store_true",
        dest="train_mode",
        help="turn on model training",
    )
    parser.add_argument(
        "--dry_run",
        action="store_true",
        dest="dry_run",
        help="Dry run mode, will not upload the results",
    )
    parser.add_argument(
        "--plot",
        action="store_true",
        dest="plot",
        help="Plot mode, will plot the results",
    )
    parser.add_argument(
        "--isolation",
        action="store_true",
        dest="isolation",
        help="Outlier detection with Isolation Forest",
    )

    # Remove declared missing arguments (e.g. model_type)
    args = vars(parser.parse_args())
    args_no_null = {k: v for k, v in args.items() if v is not None}

    return args_no_null


def setup_params(args=None):
    """Manage setup parameters."""
    if args is None:
        args = {}

    # Get program call arguments
    params = args.copy()

    # Update parameters with constants
    if params["debug_mode"]:
        params.update(project_parameters_debug)
    else:
        params.update(project_parameters)
    params["version"] = toml.load("pyproject.toml")["tool"]["poetry"]["version"]

    params["session_id"] = ulid(params["project_hash"])
    logger.info(f"Session id is: {params['session_id']}")

    runtime_keys = list(set(list(args.keys()) + ["session_id", "version"]))

    # Directories and paths
    os.makedirs(params["folder_data"], exist_ok=True)
    os.makedirs(params["folder_plot"], exist_ok=True)
    params[
        "path_g_app_cred"
    ] = f"{params['folder_secrets']}/{params['file_g_app_cred']}"

    for file in ["train_data_file", "test_data_file"]:
        params[f"path_{file}"] = f"{params['folder_data']}/{params[file]}"

    # Create a path for feature transformer if needed
    if "ft_file" in params:
        params["path_ft_file"] = f"{params['folder_data']}/{params['ft_file']}"

    # Derived parameters and format checks (depends on train / test mode)
    if params["train_mode"]:
        # Force stop run if model_type is not specified
        if "model_type" not in params or params["model_type"] not in [
            "hgb",
            "cat",
            "lsq",
            "opt",
            "catrf",
            "rf",
        ]:
            msg = "Model_type is not properly specified: cannot run train mode"
            logger.error(msg)
            insert_logs(params, msg)
            sys.exit(1)

        params["model_id"] = params["session_id"]

    else:
        # Force stop run if model_id is not specified
        if not params["model_id"]:
            msg = "Model_id is not specified: cannot run test mode"
            logger.error(msg)
            insert_logs(params, msg)
            sys.exit(1)

        # Fetch model parameters from GBQ
        logger.info("Getting model parameters from DWH")
        run_list = q_runs(params)

        params_gbq = {}
        # We allow empy gbq parameters since reporting runs does not require model_id
        try:
            params_gbq = json.loads(run_list.parameters.iloc[0])
        except IndexError:
            logger.warning("Model id is not found in DWH")

        # Keep runtime parameters from test run
        for field in runtime_keys:
            if not field.startswith("path"):
                params_gbq[field] = params[field]
        params.update(params_gbq)

        # Update parameters from env file
        secret_path = f'{params["folder_secrets"]}/{params["env_file"]}'
        if os.path.exists(secret_path):
            import_env = dotenv_values(secret_path)
            import_env = {k.lower(): v for k, v in import_env.items()}
            params.update(import_env)

        else:
            # Return an error if the file doesn't exist
            logger.warning(f"File {secret_path} does not exist...")

    # Model_id dependent paths
    params[
        "path_base_gcs"
    ] = f"{params['gcs_model_folder']}/{params['model_id']}-{params['project_name']}"
    params[
        "path_base_gcs_train_data"
    ] = f"{params['gcs_train_data_folder']}/{params['model_id']}-{params['project_name']}"
    params[
        "path_base_gcs_test_data"
    ] = f"{params['gcs_test_data_folder']}/{params['session_id']}-{params['project_name']}"
    params[
        "path_bucket_test_data"
    ] = f"{params['path_base_gcs_test_data']}-{params['test_data_file']}"
    params[
        "path_bucket_train_data"
    ] = f"{params['path_base_gcs_train_data']}-{params['train_data_file']}"

    # Create local and bucket path for model based on the model_type
    if "model_type" in params and params["model_type"] in ["hgb", "cat", "lsq", "catrf", "rf"]:
        m_t = params["model_type"]
        params[f"model_params_{m_t}"][
            "path_model_file"
        ] = f"{params['folder_data']}/{params[f'model_params_{m_t}']['model_file']}"
        params[f"model_params_{m_t}"][
            "path_bucket_model"
        ] = f"{params['path_base_gcs']}-{params[f'model_params_{m_t}']['model_file']}"

    # Create a bucket path for feature transformer if needed
    if "path_ft_file" in params:
        params["path_bucket_ft"] = f"{params['path_base_gcs']}-{params['ft_file']}"

    return params


def train_to_test(u_args, params):
    """Convert input parameters from train to test setup."""
    u_args["model_id"] = params["session_id"]
    u_args["train_mode"] = False
    u_args["dry_run"] = True
    return u_args


def load_from_env_var():
    """Load variables from environment (if needed)."""
    env_var = {
        "slack_client_secret": os.getenv("slack_client_secret"),
        "slack_signing_secret": os.getenv("slack_signing_secret"),
        "slack_bot_oauth_secret": os.getenv("slack_bot_oauth_secret"),
    }
    return env_var
