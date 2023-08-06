"""Query related functions."""

from .io import get_bq_client, logger


def q_runs(params):
    """Query parameters from previous runs."""
    query = f"""
    SELECT
        parameters
    FROM `{params['google_project_id']}.{params['gbq_db_schema_metrics']}.{params['gbq_db_table_metrics']}`

    WHERE session_id = '{params['model_id']}'
    """

    client, job_config = get_bq_client(params)
    res = client.query(query, job_config=job_config).to_dataframe(
        progress_bar_type="tqdm"
    )

    return res


def q_delete_run(params, model_id):
    """Query parameters from previous runs."""
    query = f"""
    DELETE
    FROM `{params['google_project_id']}.{params['gbq_db_schema_metrics']}.{params['gbq_db_table_metrics']}`
    WHERE session_id = '{model_id}'
    """

    client, job_config = get_bq_client(params)
    try:
        _ = client.query(query=query, job_config=job_config)
        logger.info(
            f"{model_id} successfully deleted from {params['gbq_db_schema_metrics']}.{params['gbq_db_table_metrics']}"
        )
    except Exception as e:
        logger.warning(e)

    return


def q_metrics(params, model_id=None):
    """Query parameters from previous runs."""
    if not model_id:
        model_id = params["model_id"]

    query = f"""
    SELECT
        metrics
    FROM `{params['google_project_id']}.{params['gbq_db_schema_metrics']}.{params['gbq_db_table_metrics']}`
    WHERE session_id = '{model_id}'
    """

    client, job_config = get_bq_client(params)
    res = client.query(query=query, job_config=job_config).to_dataframe(
        progress_bar_type="tqdm"
    )

    return res


def q_runs_all(params):
    """Query parameters from previous runs."""
    query = f"""
    SELECT
        parameters
    FROM `{params['google_project_id']}.{params['gbq_db_schema_metrics']}.{params['gbq_db_table_metrics']}`
    WHERE project_name = '{params['project_name']}'
    """

    client, job_config = get_bq_client(params)
    res = client.query(query=query, job_config=job_config).to_dataframe(
        progress_bar_type="tqdm"
    )

    return res
