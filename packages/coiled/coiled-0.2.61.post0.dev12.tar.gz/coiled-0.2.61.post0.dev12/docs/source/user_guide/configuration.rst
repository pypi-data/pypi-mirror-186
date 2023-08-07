=============
Configuration
=============

Coiled uses Dask's built-in configuration system. You can set a number of configuration settings, including:

#. Coiled account settings
#. Cluster hardware
#. Customization of Dask scheduler or workers
#. Dask configuration

Coiled account settings
-----------------------

The ``coiled login`` command line tool (see :ref:`coiled-login-cli`) automatically creates and populates the ``~/.config/dask/coiled.yaml`` configuration file with the following:

.. code-block:: yaml

    coiled:
      account: "<your account>"
      server: https://cloud.coiled.io
      token: "<your token>"             
      user: "<your username>"

You can change any of these values directly by editing your local ``~/.config/dask/coiled.yaml`` yaml file.

.. dropdown:: Coiled configuration default yaml file

  .. literalinclude:: ../../../coiled/coiled.yaml
    :language: yaml

For most login options, you can use the CLI tool to set these values, depending on the value you would like to change. To change your default account, for example, you can use ``coiled login --account``.

Cluster infrastructure/hardware
-------------------------------

There are a number of cluster infrastructure and hardware settings you can configure, including:

- Instance types (see :doc:`tutorials/select_instance_types`)
- Custom network security (see :doc:`tutorials/bring_your_own_network` and :doc:`tutorials/configuring_firewalls`)
- Cloud provider-specific configuration, e.g. whether to use Spot instances or selecting a region (see :ref:`aws_backend_options` for AWS or :ref:`gcp_backend_options` for Google Cloud)

Customization of Dask scheduler and workers
-------------------------------------------

There are a number of keyword arguments you can pass to the Dask :class:`Scheduler class <distributed.scheduler.Scheduler>` and :class:`Worker class <distributed.worker.Worker>`. A number of these arguments are handled by Coiled, however, a few common use cases for Coiled users include: 

- Setting the idle timeout for the scheduler (see :ref:`idle-timeout`)
- Setting the number of threads per worker (see :ref:`set-threads-per-worker`)
- Specify Dask resources to constrain how your tasks run on your workers (see :ref:`set-worker-resources`)

You can set these when making a Coiled cluster using ``scheduler_options`` and ``worker_options`` keyword arguments on ``coiled.Cluster`` (see :ref:`customize-cluster`).

Dask configuration
------------------

`Dask configuration <https://docs.dask.org/en/stable/configuration.html>`_ controls a variety of options for customizing Dask's behavior. For example, you can use this to `control memory thresholds where Dask will spill to disk <https://distributed.dask.org/en/stable/worker-memory.html#thresholds-configuration>`_ or to `adjust task queuing <https://distributed.dask.org/en/latest/scheduling-policies.html#adjusting-or-disabling-queuing>`_. Other packages in the Dask ecosystem also make use of the Dask configuration system for exposing various options (e.g. `Dask-jobqueue <https://jobqueue.dask.org/en/latest/>`_, `Dask Cloud Provider <https://cloudprovider.dask.org/en/latest/index.html>`_).

Since Coiled uses Dask's configuration system, you can set these values in any of the ways you usually would when using Dask locally:

- Configuration yaml files in ``~/.config/dask/``
- Environment variables
- Directly in Python code using ``dask.config``

When you start a Coiled cluster by calling ``coiled.Cluster``, we get all of the configuration values set in your local environment and ship these to your cluster. 
    
.. note::
    Changes made to local YAML files or environment variables will not affect already running clusters. To change a configuration value after your cluster is already running, the best way is to use ``dask.config.set``.

In addition to Dask-specific configuration, you can also use any of the above methods to set Coiled-specific configuration values.

.. list-table:: Equivalent ways of setting commonly used configuration values
   :widths: 15 25 15 50
   :header-rows: 1

   * - YAML Key
     - Environment variable
     - ``dask.config.set``
     - Description
   * - ``account``
     - ``DASK_COILED__ACCOUNT``
     - ``dask.config.set({"coiled.account": <your-account-name>})``
     - The Coiled account you want to use.
   * - ``token``
     - ``DASK_COILED__TOKEN``
     - ``dask.config.set({"coiled.token": <your-token>})``
     - The Coiled token for your personal account.
   * - ``software``  
     - ``DASK_COILED__SOFTWARE``
     - ``dask.config.set({"coiled.software": <your-senv-name>})``
     - Name of the software environment to use.
