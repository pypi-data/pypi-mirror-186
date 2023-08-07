import dask
from dask.distributed import Client
from prefect import flow, get_run_logger, task

import coiled


@task
def load_data():
    """Load some data"""
    return dask.datasets.timeseries("2000", "2005", partition_freq="2w").persist()


@task
def summarize(df):
    """Compute a summary table"""
    return df.groupby("name").aggregate({"x": "sum", "y": "max"}).compute()


@task
def log_summary(df):
    """Log summary result"""
    logger = get_run_logger()
    logger.info(df)


@flow
def timeseries_flow():
    df = load_data()
    summary_df = summarize(df)
    log_summary(summary_df)


if __name__ == "__main__":

    with coiled.Cluster(
        name="prefect-timeseries", n_workers=5, software="prefect2-example"
    ) as cluster:
        client = Client(cluster)
        timeseries_flow()
