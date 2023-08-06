"""Config constant params for data science project(s)."""

project_parameters = {
    # Code version
    "version": "1.0.0",
    # Google related parameters
    "google_project_id": "data-pipeline-276214",
    "gcs_bucket": "forto-data-science",
    "gcs_model_folder": "model-collection",
    "gcs_train_data_folder": "train-data-collection",
    "gcs_test_data_folder": "test-data-collection",
    "gbq_db_schema_log": "data_science",
    "gbq_db_table_log": "logs",
    "gbq_db_schema_metrics": "data_science",
    "gbq_db_table_metrics": "runs",
    # Project specific values
    "project_hash": "",
    "project_name": "",
    # Formats
    "date_fmt": "%Y-%m-%d",
    "datetime_fmt": "%Y-%m-%dT%H:%M:%SZ",
    "fig_size": (18, 10),
    # Paths
    "env_file": ".env",
    "folder_data": "data",
    "folder_secrets": "secrets",
    "folder_plot": "plot",
    "file_plot_name": "scatter_plot.png",
    "file_g_app_cred": "google_access.json",
    # Query constants
    "debug_row_limit": 10000,
    "insertion_chunk_size": 512,
    # ETL constants
    "ft_file": "feature_transformer.pkl.gz",
    "train_data_file": "train_val_data.pkl.gz",
    "test_data_file": "test_data.pkl.gz",
    "abs_corr_collinearity": 0.9,
    "na_replace_val": -0.42069,
    "random_state": 42,
    "train_test_split": 0.75,
    "id_field": "shipment_id",
    "is_date_date_ratio": 0.1,
    "is_numeric_nan_count_mean": 0.1,
    "nan_value_percentage": 0.9,
    "if_n_estimators": 650,
    "if_sr_isolation": 0.05,
    "if_contamination": 0.135,
    "extract_feature_per_shipment_single": True,
    "validation_test_split": True,  # For 3 splits
    # Data Constants
    "data_n_output": "",
    # Model training constants
    "model_params_hgb": {
        "max_iter": 500,
        "max_leaf_nodes": 31,
        "l2_regularization": 0,
        "loss": "log_loss",
        "scoring": "loss",
        "learning_rate": 0.01,
        "early_stopping": True,
        "tol": 1e-6,
        "n_iter_no_change": 30,
        "random_state": 42,
        "verbose": 1,
        "model_file": "tree.pkl.gz",
    },
    "model_params_cat": {
        "model_file": "cat.pkl.gz",
    },
}
