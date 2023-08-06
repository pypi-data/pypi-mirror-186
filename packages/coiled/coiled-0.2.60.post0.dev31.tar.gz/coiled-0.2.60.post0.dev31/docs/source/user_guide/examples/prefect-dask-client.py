import dask
from prefect import flow, task
from prefect_dask import DaskTaskRunner, get_dask_client


@task
def compute_task():
    with get_dask_client() as client:  # noqa
        df = dask.datasets.timeseries("2000", "2001", partition_freq="4w")
        summary_df = df.describe().compute()
    return summary_df


@flow(
    task_runner=DaskTaskRunner(
        cluster_class="coiled.Cluster",
        cluster_kwargs={
            "name": "",
            "n_workers": 4,
            "software": "prefect2-example",
        },
    )
)
def dask_flow():
    prefect_future = compute_task.submit()
    return prefect_future.result()


if __name__ == "__main__":
    dask_flow()
