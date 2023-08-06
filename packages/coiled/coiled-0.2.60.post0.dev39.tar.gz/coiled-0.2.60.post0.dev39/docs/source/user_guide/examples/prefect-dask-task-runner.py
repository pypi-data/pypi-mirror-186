from prefect import flow, task
from prefect_dask import DaskTaskRunner

coiled_runner = DaskTaskRunner(
    cluster_class="coiled.Cluster",
    cluster_kwargs={
        "n_workers": 5,
        "software": "prefect2-example",
        "name": "prefect-dask-runner",
    },
)


@task
def inc(x):
    return x + 1


@task
def double(x):
    return x * 2


@task
def add(x, y):
    return x + y


@task
def sum_all(z):
    return sum(z)


@flow(task_runner=coiled_runner)
def inc_double_add_sum(a_range):
    a = inc.map(a_range)
    b = double.map(a_range)
    c = add.map(x=a, y=b)
    return sum_all(c)


if __name__ == "__main__":
    inc_double_add_sum(range(10))
