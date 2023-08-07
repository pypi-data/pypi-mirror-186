=================
Creating clusters
=================

.. currentmodule:: coiled

There are a number of options for customizing your Coiled cluster. Each of the sections below serve as a how-to guide for :class:`coiled.Cluster` customization. 

Cluster resources
-----------------

You can specify a number of resources (e.g. number of workers, CPUs, memory) and Coiled will request a cluster with the matching specifications from your cloud provider (see :doc:`tutorials/select_instance_types`). Coiled also supports using ARM (Graviton) instances on AWS (see :doc:`tutorials/arm`).

.. list-table::
   :widths: 25 50 25
   :header-rows: 1

   * - Parameter
     - Description
     - Default
   * - ``n_workers``
     - Number of workers in the cluster.
     - ``4``
   * - ``worker_cpu``
     - Number (or range) of CPUs requested for each worker
     - ``None``
   * - ``worker_gpu``
     - Number of GPUs requested for each worker. See :doc:`gpu`.
     - ``0``
   * - ``worker_memory``
     - Amount of memory to request for each worker
     - ``None``
   * - ``scheduler_cpu``
     - Number (or range) of CPUs requested for the scheduler
     - ``None``
   * - ``scheduler_memory``
     - Amount of memory to request for the scheduler
     - ``None``
    
When specifying CPU or memory requirements, you can pass a range of values or a single value. For example:

.. code-block:: python

    import coiled

    cluster = coiled.Cluster(worker_cpu=[2, 8], scheduler_memory=["2GiB", "10GiB"])

You can also specify a list of specific instance types. Since cloud providers may have availability issues for a specific instance type, it's recommended you specify more than one type in the list.

.. list-table::
   :widths: 25 50 25
   :header-rows: 1

   * - Parameter
     - Description
     - Default
   * - ``worker_vm_types``
     - List of instance types for the workers
     - ``["t3.xlarge/e2-standard-4"]``
   * - ``scheduler_vm_types``
     - List of instance types for the scheduler
     - ``["t3.xlarge/e2-standard-4"]``

.. note::

    You can specify memory and CPU **or** specific instance types, but not a combination of both. The ``worker_vm_types`` argument, for example, should not be used with either ``worker_memory`` or ``worker_cpu``.

.. _cluster-pricing-kwargs:

Pricing and availability
^^^^^^^^^^^^^^^^^^^^^^^^

AWS and Google Cloud both offer Spot instances at substantially lower costs (see the `AWS Spot <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html>`_ and `Google Cloud Spot <https://cloud.google.com/compute/docs/instances/spot>`_ documentation). You can specify whether to request Spot instances by passing one of "on-demand" (default), "spot", or "spot_with_fallback" to the ``compute_purchase_option`` keyword argument, where "spot_with_fallback" permits using on-demand instances as needed if the requested Spot instances are unavailable.

.. note::
    For AWS, there is graceful shutdown and replacement of spot instances to minimize interruptions. This feature is still in development for Google Cloud, in part due to the relatively shorter notice for termination from Google Cloud.

Spot instances can be harder to get. You can set ``use_best_zone=True`` when creating a Coiled cluster to allow your cloud provider to pick the best availability zone (inside your selected region). This argument also helps increase the chances of obtaining harder-to-get instance types.


.. list-table::
   :widths: 20 60 20
   :header-rows: 1

   * - Parameter
     - Description
     - Default
   * - ``compute_purchase_option``
     - Purchase option to use for workers in your cluster.
       Options are "on-demand", "spot", and "spot_with_fallback".
       Google Cloud refers to this as the "provisioning model" for your instances.
     - ``on-demand``
   * - ``use_best_zone``
     - Allow the cloud provider to pick the zone (in your specified region)
       that has best availability for your requested instances. We'll keep the scheduler and workers all in a single zone in order to avoid any interzone network traffic (which would be billed).
     - ``True``
    
You can combine these arguments to minimize cost and maximize availability:

.. code-block:: python

    import coiled

    cluster = coiled.Cluster(
        use_best_zone=True, compute_purchase_option="spot_with_fallback"
    )


Python environment
------------------

The scheduler and workers in a Coiled cluster are all launched with the same python environment. Once you've created an environment, you can use the ``software`` keyword argument to use it on your cluster (see :doc:`software_environment`). For example, if you've created an environment named ``scaling-xgboost`` in your Coiled account, you can create a cluster that uses this environment:

.. code-block:: python

    import coiled

    cluster = coiled.Cluster(software="<my-account>/scaling-xgboost")


.. _customize-cluster:

Custom workers and scheduler
----------------------------

Dask supports using custom worker and scheduler classes. There are some use cases where this can allow for increased functionality (e.g. `Dask-CUDA <https://dask-cuda.readthedocs.io>`_'s ``CUDAWorker`` class for running Dask workers on NVIDIA GPUs). Additionally, scheduler and worker classes also have their own keyword arguments that can be specified to control their behavior (see the :class:`Scheduler class <distributed.scheduler.Scheduler>` and :class:`Worker class <distributed.worker.Worker>`, respectively).

.. list-table::
   :widths: 25 50 25
   :header-rows: 1

   * - Parameter
     - Description
     - Default
   * - ``worker_class``
     - Class to use for cluster workers
     - ``"distributed.Nanny"``
   * - ``worker_options``
     - Mapping with keyword arguments to pass to ``worker_class``
     - ``{}``
   * - ``scheduler_class``
     - Class to use for the cluster scheduler
     - ``"distributed.Scheduler"``
   * - ``scheduler_options``
     - Mapping with keyword arguments to pass to ``scheduler_class``
     - ``{}``

For example, the following creates a cluster which uses Distributed's :class:`Worker class <distributed.worker.Worker>` class for workers (instead of the default :class:`Nanny class <distributed.nanny.Nanny>`):

.. code-block:: python

    import coiled

    cluster = coiled.Cluster(worker_class="distributed.Worker")

.. _idle-timeout:

Customizing idle timeout
^^^^^^^^^^^^^^^^^^^^^^^^

Any Coiled cluster you create will automatically shut down after 20 minutes of inactivity. You can customize this setting with ``scheduler_options``. In the following example, you can set the ``idle_timeout`` to 2 hours:

.. code-block:: python

    import coiled

    cluster = coiled.Cluster(scheduler_options={"idle_timeout": "2 hours"})


.. _set-threads-per-worker:

Setting threads per worker
^^^^^^^^^^^^^^^^^^^^^^^^^^

By default, a worker will use as many threads as a node has cores. This allows the worker to run many computations in parallel. You can limit the number of threads a worker can use with the ``worker_options`` keyword argument. If you set the number of threads to one, it will allow the worker to run computations mostly synchronously.

.. code:: python

    import coiled

    cluster = coiled.Cluster(worker_options={"nthreads": 1})

.. _set-worker-resources:

Setting Dask worker resources
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Dask allows you to specify abstract arbitrary "resources" to constrain how your tasks run on your workers.
A common reason to use this is if you have (say) two GPUs per worker and want to constrain certain tasks (the ones that use the GPU) to run at most two concurrent instances on any worker.
More generally, for any arbitrary "foo" you can specify the quantity of "foo" that each worker has and the quantity that certain tasks use.

For more information about the general idea, see the `Dask documentation on worker resources <https://distributed.dask.org/en/stable/resources.html>`_.

If you want to use Dask worker resources, you can set "available" resources on a worker when you create a Coiled cluster using ``worker_options``, for example:

.. code:: python

    import coiled

    # tell your workers how many resources they have available
    cluster = coiled.Cluster(worker_options={"resources": {"GPU": 2}})

Next, you need to tell Dask how much of a given resource each task needs. If you're using the Futures API, you can do this with the ``resources`` keyword argument (see the `Dask documentation for an example using client.submit <https://distributed.dask.org/en/stable/resources.html#resources-are-applied-separately-to-each-worker-process>`_). If you're using a Dask collection (e.g. arrays, dataframes, or delayed objects) you can annotate the operations where resources should be restricted (see the `Dask documentation for an example using collections <https://distributed.dask.org/en/stable/resources.html#resources-with-collections>`_).

Backend options
---------------

You can use the ``backend_options`` keyword argument when creating a cluster to customize options that are specific to your cloud provider (e.g. which AWS region to use). You can pass a dictionary of cloud provider-specific options, for example:

.. code-block:: python

    import coiled

    # set the region for AWS
    cluster = coiled.Cluster(backend_options={"region_name": "us-east-2"})

See :ref:`AWS reference <aws_backend_options>` and :ref:`Google Cloud reference <gcp_backend_options>` for a list of options.

Environment Variables
---------------------

.. attention::

    Environment variables are not encrypted and will be available as plain text. For security reasons, you should **not** use environment variables to add secrets to your clusters.

To add environment variables to your clusters, use the ``environ`` keyword argument of ``coiled.Cluster``. ``environ`` accepts a dictionary, for example:

.. code-block:: python

    import coiled

    cluster = coiled.Cluster(
        n_workers=5,
        environ={
            "DASK_COILED__ACCOUNT": "alice",
            "DASK_DISTRIBUTED__SCHEDULER__WORK_STEALING": True,
            "DASK_DISTRIBUTED__LOGGING__DISTRIBUTED": "info",
        },
    )

.. _cluster-tags:

Tags
----

You can set custom tags for your cluster, which can be helpful for tracking resources in your cloud provider account (see :doc:`tutorials/resources_created_by_coiled`). To tag your cluster, use the ``tags``
keyword argument of ``coiled.Cluster``. The input of ``tags`` should be a dictionary where both keys and values are strings, for example:

.. code-block:: python

    import coiled

    cluster = coiled.Cluster(
        n_workers=5,
        tags={
            "Team": "Product",
            "Environment": "Development",
        },
    )

.. note::

    Coiled applies a custom set of tags to every instance which can't be overridden. These include ``owner``, ``account``, and a number of tags beginning with ``coiled-``.

.. _blocked-ports:

Working around blocked ports
----------------------------

In some cases, the default port 8786 used for communication between your Dask client (from which you submit code) and the Coiled Dask scheduler (running in the cloud) may be blocked (see :ref:`communication-dask-clusters`). Binder blocks port 8786, for example, as do some corporate networks.

If this is the case, you would likely get an error from the client that it's unable to connect to the ``tls://<scheduler address>:8786``, e.g.:

.. code-block:: pytb

    OSError: Timed out trying to connect to tls://54.212.201.147:8786 after 5 s

You can also check if port 8786 is blocked by trying to load http://portquiz.net:8786 on your local machine.

The easiest solution is to use a different port for communication between the client and scheduler. In the following example, you can use port 443, which is usually not blocked since it is used for HTTPS. When you specify the ``scheduler_port``, we'll open this port on the cluster firewall and tell the Dask scheduler to use this port.

.. code-block:: python

    import coiled

    cluster = coiled.Cluster(
        n_workers=1,
        scheduler_port=443,
    )


.. _wait-for-workers:

Waiting for workers
-------------------

By default, Coiled will wait for 30% of your requested workers. You can customize this behavior with the ``wait_for_workers`` parameter. You can pass an integer to wait for a specific number of workers, a fraction between 0 and 1 to wait for a proportion of workers, or a boolean to wait for all or no workers.

For example, you can use ``wait_for_workers=False`` to not wait for any workers:

.. code-block:: python

  import coiled

  cluster = coiled.Cluster(n_workers=25, wait_for_workers=False)

.. note::

    Waiting for all workers with ``wait_for_workers=True`` should be used with caution when requesting large clusters, due to availability issues from your chosen cloud provider.

You can also set ``wait_for_workers`` in your :doc:`Coiled configuration file <configuration>`:

.. code-block:: yaml

    # ~/.config/dask/coiled.yaml

    coiled:
      wait_for_workers: false
