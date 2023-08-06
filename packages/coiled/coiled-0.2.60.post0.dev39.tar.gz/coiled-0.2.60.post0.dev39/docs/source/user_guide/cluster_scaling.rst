================
Scaling clusters
================

.. currentmodule:: coiled

Manual scaling
--------------

After you've created a cluster with Coiled, you can scale it up or down using :meth:`coiled.Cluster.scale()`. Since there is a delay between requesting to scale a cluster and when workers are added or removed, you can pair this with :meth:`Client.wait_for_workers <distributed.Client.wait_for_workers()>`.

In the following example, you can start a cluster with 10 workers, scale it up to 15 workers, and then submit the blocking call to wait to continue until 15 workers have been allocated.

.. code-block:: python

   import coiled
   from dask.distributed import Client

   cluster = coiled.Cluster(n_workers=10)
   client = Client(cluster)

   cluster.scale(15)
   client.wait_for_workers(15)

You can also monitor your cluster as workers are added or removed on the cluster details page at ``https://cloud.coiled.io/<your-account>/clusters/<your-cluster-id>/details`` (see :ref:`coiled-cloud`).

Adaptive scaling
----------------

You can use :meth:`coiled.Cluster.adapt()` to let the scheduler decide how many workers it should create (or destroy) depending on the workload. With adaptive scaling, you can specify a range of requested workers and the Dask scheduler will handle scaling the cluster up or down for you (see `Adaptive Deployments in the Dask docs <https://docs.dask.org/en/latest/setup/adaptive.html>`_).

In the following example, you can create a cluster and set the minimum number of workers

.. code-block:: python

   import coiled
   from dask.distributed import Client

   cluster = coiled.Cluster()
   client = Client(cluster)

   cluster.adapt(minimum=10, maximum=40)


.. note::

   Coiled will not exceed the core limit set in your Coiled account, and will stop adding workers to your cluster once the limit is reached. You can use :meth:`coiled.list_core_usage()` to see core limits.

