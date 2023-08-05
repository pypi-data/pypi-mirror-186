==================================
Set up a custom Python environment
==================================

This tutorial will go through creating a custom local Python environment that is in sync with a Coiled Python environment. It is important that the packages installed on your local machine are the same as in the cloud computing environment where the Dask clusters are created (see :doc:`../software_environment_local` for more information).

.. figure:: ../images/coiled-architecture.png
   :width: 100%
   :alt: Coiled Architecture

   Coiled Architecture (click image to enlarge)

Installing software can be challenging due to the combinations of various requirements, dependencies, and configurations. To simplify this process, we can use the `coiled-runtime metapackage <https://github.com/coiled/coiled-runtime>`_ with the recommended versions of Dask and associated packages to get started (see the :ref:`overview on coiled-runtime <coiled-runtime>` for more information).

.. note::

    Coiled has a feature called package sync which scans your local Python environment and replicates it to the cluster, so you no longer need to go through the extra step of creating a Coiled software environment. See :doc:`../package_sync` for more details.

Create the environment locally
------------------------------

In the :doc:`Getting Started page <../getting_started>`, you created the ``coiled/default`` environment locally. Though this is a great way to get started quickly, as a next step we recommend creating a custom environment specific to the needs of your project. One way to do this is using an ``environment.yml`` file and conda.

Start by copying and pasting the following into a file named ``environment.yml``, replacing ``<x.x.x>`` with the versions you would like to use and optionally including any other packages you need in the list of dependencies. You can get most up-to-date version of coiled-runtime from the latest `tag <https://github.com/coiled/coiled-runtime/tags>`_ in the public coiled-runtime repository. Python versions 3.7, 3.8, and 3.9 are currently supported (see `software environments yaml file <https://github.com/coiled/coiled-runtime/blob/304ae9db862e23d38f17d73ce7a3f7ca965eeff2/.github/workflows/software-environments.yml#L16>`_ in the coiled-runtime repository).

.. code:: yaml

    channels:
      - conda-forge
    dependencies:
      - coiled-runtime=<x.x.x>
      - python=<x.x.x>

If you wanted to include XGBoost, use Python version 3.9, and coiled-runtime version 0.0.3, the ``environment.yml`` file would look like the following example. In case you would like to include packages that are not available on conda-forge, you can also use pip.

.. code:: yaml

    channels:
      - conda-forge
    dependencies:
      - coiled-runtime=0.0.3
      - python=3.9
      - xgboost=1.5.1
      # uncomment the lines below for installing packages with pip
      # - pip
      # - pip:
        # - <pip-only-installable-package>

Run the code snippet below in your terminal to create and activate the same environment locally. In this example, the environment is named ``my-env-py39`` (set with the ``-n`` flag). The environment name should only contain ASCII letters, hyphens, and underscores and be something that will help you remember which project it will be used for. It is conventional to include the python version at the end, but not required.

.. code:: bash

    $ conda env create -f environment.yml -n my-env-py39
    $ conda activate my-env-py39

Create the environment on the cloud
-----------------------------------

Next create this same environment to be used in the cloud computing environment using the ``coiled env create`` command line tool:

.. code:: bash

    $ coiled env create -n my-env-py39 --conda environment.yml

This is one of many ways Coiled supports creating software environments on the cloud computing environment. For a comprehensive overview see the documentation on :doc:`creating software environments </user_guide/software_environment_creation>`.

Now you can launch a Dask cluster with this environment, replacing ``software="my-env-py39"`` with the name of your software environment:

.. code:: python

    import coiled

    cluster = coiled.Cluster(software="my-env-py39")

    cluster.close()


Next Steps
----------

In this tutorial, you created a custom software environment by relying on the `coiled-runtime metapackage <https://github.com/coiled/coiled-runtime>`_. There are a number of tools available for Python environment management and these tools work well with Coiled to ensure consistency between local and remote environments.

Now that you have your custom environment set up, you may want to check out the documentation on :doc:`creating and managing Dask clusters </user_guide/cluster>`. For more advanced techniques on Python environment management, follow our guide on :doc:`upload_file_to_coiled`.
