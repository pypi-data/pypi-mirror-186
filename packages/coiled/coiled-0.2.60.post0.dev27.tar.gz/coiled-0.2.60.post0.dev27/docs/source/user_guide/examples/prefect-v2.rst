:orphan:

Workflow automation with Prefect 2
==================================

`Prefect <https://www.prefect.io/>`_ is a workflow management system
you can use to automate your data pipelines. Prefect is built on
top of Dask, so you can execute workflows in parallel and
use Coiled to execute those workflows on the cloud.

In this example, you'll learn two main ways to use Coiled with Prefect:

#. Let Dask determine when and where to run the computation within each task and use Prefect to manage your flow and launch tasks sequentially. This method is recommended when working with Dask collections (e.g. Dask DataFrame).
#. Execute Prefect tasks with the ``DaskTaskRunner``, using Dask to determine when and where to run all tasks in your flow.

Before you start
~~~~~~~~~~~~~~~~

1. Create your Python environment
---------------------------------

You'll first need to create consistent local and remote software environments
with ``dask``, ``coiled``, ``prefect``, and the necessary dependencies installed.
If you are unfamiliar with creating software environments, you can first
follow the
:doc:`tutorial on setting up a custom software environment <../tutorials/matching_coiled_senvs>`.

First, you will install :ref:`coiled-runtime <coiled-runtime>`, a Dask meta-package, and ``prefect``.
Save the following file as ``environment.yml``, replacing ``<x.x.x>`` with the versions
you would like to use. You can get the most up-to-date version of coiled-runtime from the
`latest tag <https://github.com/coiled/coiled-runtime/tags>`_.

.. code:: yaml

   channels:
     - conda-forge
   dependencies:
     - coiled-runtime=<x.x.x>
     - python=3.9
     - pip
     - pip:
       - prefect>=2.0
       - prefect-dask>=0.2.1

Next, create a local environment using the ``environment.yml`` file:

.. code:: bash

    $ conda env create -f environment.yml -n prefect2-example
    $ conda activate prefect2-example

Lastly, create a remote software environment using the ``environment.yml`` file:

.. code:: bash

    $ coiled env create -n prefect2-example --conda environment.yml


2. Set up Prefect Cloud
-----------------------

Coiled works best when used with Prefect Cloud, a coordination-as-a-service platform. You can follow `these instructions from Prefect <https://docs.prefect.io/ui/cloud-getting-started/>`_ on how to get started for free.

Terminology
~~~~~~~~~~~

In this example, you'll see three key Prefect terms: ``flows``, ``tasks``, and ``task runners``.
A `flow <https://docs.prefect.io/concepts/flows/>`_
is a collection of individual steps, or `tasks <https://docs.prefect.io/concepts/tasks/>`_.
A task is similar to a function; it accepts arguments, does something with them, and
optionally returns a result. `Task runners <https://docs.prefect.io/concepts/task-runners/>`_ are optional and allow you to choose whether Prefect executes tasks sequentially, concurrently, or in parallel.

.. _prefect-no-runner:

Working with Dask collections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this example, you'll perform some common data manipulation operations on a Dask DataFrame and log a summary result (:download:`download the complete example <prefect-no-runner.py>`).

You'll use Prefect to define three ``tasks`` with the ``@task`` decorator:

#. ``load_data`` uses Dask to lazily read in a random timeseries of data from ``dask.datasets``.
#. ``summarize`` uses Dask to compute aggregations of multiple columns. 
#. ``log_summary`` uses the Prefect logger to log the result of ``summarize``.

.. literalinclude:: prefect-no-runner.py
    :lines: 1-24

The three tasks are put together to build a ``flow``:

.. literalinclude:: prefect-no-runner.py
    :lines: 25-32

Now you can run your ``flow`` within the Coiled cluster context:

.. literalinclude:: prefect-no-runner.py
    :lines: 32-38

You've just used Prefect to execute each ``task`` in your ``flow`` and you let Dask determine the best way to perform individual computations within a Prefect ``task``, i.e. reading in a dataset and calculating some summary statistics. You used Coiled to manage deployment of all this in your cloud provider account.

.. _prefect-dask-task-runner:

Executing Prefect tasks with Dask
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With Prefect's `DaskTaskRunner <https://prefecthq.github.io/prefect-dask/>`_, you can use the ``dask.distributed`` scheduler to decide where and when to run your Prefect ``tasks`` (:download:`download the complete example <prefect-dask-task-runner.py>`).

In this example, you'll define the following ``tasks`` with the ``@task`` decorator:

.. literalinclude:: prefect-dask-task-runner.py
    :lines: 13-32

And combine these ``tasks`` into a ``flow`` with the ``@flow`` decorator:

.. literalinclude:: prefect-dask-task-runner.py
    :lines: 33-40

The ``inc`` and ``double`` tasks are mapped over ``a_range``, in this case, a sequence of integers 0 through 9.
Then, ``add`` is mapped over the results from ``inc`` and ``double``. Lastly ``sum_all`` reduces the sequence
of integers to a single value by summing all elements. There is parallelism in these tasks, since ``inc``, ``double``, and ``add`` can be evaluated independently.

Now that you have defined the ``flow``, you can use the ``DaskTaskRunner`` with Coiled to run this flow in the cloud:

.. literalinclude:: prefect-dask-task-runner.py
    :lines: 3-12

You can also choose to connect to an already existing cluster by using the same Coiled cluster name (see our page on :doc:`../cluster_reuse`) or by using the scheduler address. For example:

.. code-block:: python

    import coiled
    from prefect_dask import DaskTaskRunner

    cluster = coiled.Cluster(...)

    task_runner = DaskTaskRunner(
        address=cluster.scheduler_address, client_kwargs={"security": cluster.security}
    )

Computing Dask collections
--------------------------

.. note::

  Dask and Prefect both use the term "task" to refer to the concept of work to be done. In this explanation, it's helpful to conceptualize a Prefect task as containing individual Dask tasks.

In some cases, you may want to use Prefect's ``DaskTaskRunner`` for tasks containing Dask collections. You can do this by submitting Dask tasks to the Dask worker with ``get_dask_client`` or ``get_async_dask_client``. See the Prefect documentation on `distributing Dask collections across workers <https://prefecthq.github.io/prefect-dask/#distributing-dask-collections-across-workers>`_ for more information. For example (:download:`download the complete example <prefect-dask-client.py>`):

.. literalinclude:: prefect-dask-client.py

It's worth noting ``get_dask_client`` is a utility function around :py:func:`distributed.worker_client`, with ``separate_thread=False``. It will invoke a Dask client on a worker and allow you to distribute that work across all workers in your cluster. There is some overhead to using ``get_dask_client``, so it is better used for longer running tasks (see the `Dask documentation on submitting tasks from a worker <https://distributed.dask.org/en/stable/task-launch.html#connection-with-context-manager>`_)

Next steps
~~~~~~~~~~

Coiled and Prefect and working together to create additional resources using Prefect 2. See this `github issue <https://github.com/coiled/feedback/issues/191>`_ to follow our progress.
