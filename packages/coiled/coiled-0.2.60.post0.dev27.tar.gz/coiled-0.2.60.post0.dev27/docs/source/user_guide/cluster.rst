=============
Dask Clusters
=============

.. currentmodule:: coiled
    
.. toctree::
    :maxdepth: 1
    :hidden:

    cluster_creation
    cluster_scaling
    cluster_reuse
    cluster_management

Coiled manages cloud resources, networking, software environments, and everything you need to scale Python in the cloud. Spinning up Dask clusters with Coiled is done by creating a :class:`coiled.Cluster` instance. ``coiled.Cluster`` objects manage a Dask cluster much like other cluster objects (e.g. :class:`distributed.LocalCluster`).

#. Launch a Dask cluster with Coiled:

   .. code-block:: python

      import coiled

      cluster = coiled.Cluster()

#. Connect to your cluster with Dask:

   .. code-block:: python

       from dask.distributed import Client

       client = Client(cluster)

#. Run your Dask computation in the cloud:

   .. code-block:: python

        import dask

        # generate random timeseries of data
        df = dask.datasets.timeseries("2000", "2005", partition_freq="2w").persist()

        # perform a groupby with an aggregation
        df.groupby("name").aggregate({"x": "sum", "y": "max"}).compute()

#. Monitor your computation in real-time using the `Dask dashboard <https://docs.dask.org/en/latest/dashboard.html>`_:

   .. code-block:: python

        print(cluster.dashboard_link)

   You can also generate :doc:`performance_reports` for later inspection or use :doc:`analytics` to monitor Dask performance across clusters.

   You can monitor your cluster status and infrastructure state using the Coiled web application by navigating to ``cloud.coiled.io/<account-name>/clusters`` and selecting the cluster name (see :ref:`coiled-cloud`):

   .. figure:: images/cloud-cluster-dashboard.png
      :width: 800px

#. Once you're done, close your cluster and the Dask client:

   .. code-block:: python

        cluster.close()
        client.close()

This overview covered some of the basics of creating a cluster, running a computation, and monitoring Dask computation and cluster status. The next sections provide a more comprehensive guide on customizing clusters and additional cluster methods.
