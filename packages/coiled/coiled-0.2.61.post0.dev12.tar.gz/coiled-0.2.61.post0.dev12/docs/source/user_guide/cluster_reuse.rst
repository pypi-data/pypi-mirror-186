================
Reusing clusters
================

.. currentmodule:: coiled

You can connect to an already running cluster using the ``name`` argument. For example, if you create the following cluster:

.. code-block:: python

    import coiled

    cluster = coiled.Cluster(
        name="production",
        n_workers=5,
        worker_cpu=2,
        worker_memory=["4 GiB", "8 GiB"],
    )

Then you can connect to the same cluster with ``coiled.Cluster(name="production")``. If there are no currently running clusters with the name "production", then Coiled will create a new cluster.

If you know you'll be reusing a cluster, you can pass ``shutdown_on_close=False`` to ``coiled.Cluster`` to keep the cluster running. This is particularly helpful when you need a long running cluster. When you're ready to close your cluster, you can use :meth:`cluster.shutdown()<coiled.Cluster.shutdown()>`. For example:

.. code-block:: python

   import coiled
   from dask.distributed import Client

   with coiled.Cluster(shutdown_on_close=False) as cluster:
       client = Client(cluster)
       # ... Dask work

   cluster.shutdown()
