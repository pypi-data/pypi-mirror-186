Using custom code on a Coiled cluster
=====================================

In our tutorial on how to :doc:`matching_coiled_senvs`, you learned the basics of creating synchronized local and remote environments. In this tutorial, you'll learn more advanced techniques for installing custom Python code on an already running cluster, using a custom Docker image to create a Coiled software environment, or running additional commands after installing a package.

Replicate your local Python environment
---------------------------------------

If you are looking to replicate your local Python environment without creating a Coiled software environment, you can use :doc:`package sync <../package_sync>`, which scans your local Python environment and replicates it to your Coiled cluster::

    from coiled import Cluster

    with Cluster(package_sync=True):
        # dask work!
        pass

Package sync is particularly helpful for quickly iterating on features or for debugging. It works for packages installed locally in editable mode (i.e. installed with ``pip install -e``) or for packages installed from GitHub. 

Install a local Python module
-----------------------------

If you have custom Python functions you would like to use on your Coiled cluster, you can upload a Python module to all of your workers using Dask's `upload_file <https://distributed.dask.org/en/latest/api.html?highlight=upload_file#distributed.Client.upload_file>`_. This sends a local file to all your worker nodes on an already running cluster. This method is particularly helpful for when you would like to use custom Python functions that haven't been packaged in your Cluster.

.. code:: python

    import coiled
    from dask.distributed import Client

    cluster = coiled.Cluster()
    client = Client(cluster)

    client.upload_file("my_script.py")


.. _custom-docker:

Use a custom Docker image
-------------------------

If you already have a Docker image with the code you would like to use on your Coiled cluster, then you may want to build a Coiled software environment using that image. If your image is stored in Docker Hub, you can pass the name to the ``container`` keyword argument, e.g.::

    import coiled
    coiled.create_software_environment(
        name="custom_container", container="rapidsai/rapidsai:latest"
    )
     
If your image is stored in Amazon Elastic Container Registry or Google Artifact Registry, you can pass the full registry URL, which for Amazon would resemble ``789111821368.dkr.ecr.us-east-2.amazonaws.com/prod/coiled-runtime-schedule``.

.. note::

    Your ability to use private images stored in Docker Hub or a cloud provider-specific registry is limited by which option you chose when initially setting up your Coiled account (see the Container Registry step for :ref:`Google Cloud <setup-gar>` or :ref:`AWS <ecr>`). For example, if you chose to store your Coiled software environments in ECR, then you will not be able to use private Docker Hub images. If you would like to be able to use both Docker Hub and ECR :doc:`reach out to us <../support>` for help.

You can also include a list of packages to install in addition to those in your specified container with the ``conda`` or ``pip`` keyword arguments. For example:

.. code-block:: python

    import coiled

    coiled.create_software_environment(
        name="custom-container",
        container="user/custom-container:latest",
        conda=["coiled-runtime"],
    )

To test that your container will run successfully on your Coiled cluster, you can run::

    docker run --rm <your_container> python -m distributed.cli.dask_spec && \
    --spec '{"cls":"dask.distributed.Scheduler", "opts":{}}'

If successful, this will start the ``dask.distributed`` scheduler (you can use CTRL+C to stop it). For example::

    > docker run --rm coiled/coiled-runtime:0.0.4-py3.9 python -m distributed.cli.dask_spec && \
      --spec '{"cls":"dask.distributed.Scheduler", "opts":{}}'

    2022-10-06 14:44:43,640 - distributed.scheduler - INFO - State start
    2022-10-06 14:44:43,656 - distributed.scheduler - INFO - Clear task state
    2022-10-06 14:44:43,658 - distributed.scheduler - INFO -   Scheduler at:    tcp://172.17.0.2:41089
    2022-10-06 14:44:43,658 - distributed.scheduler - INFO -   dashboard at:                     :8787

If not, you will see an error like ``/opt/conda/bin/python: Error while finding module specification for 'distributed.cli.dask_spec' (ModuleNotFoundError: No module named 'distributed')``. For example::

    > docker run --rm continuumio/miniconda3:latest python -m distributed.cli.dask_spec && \
      --spec '{"cls":"dask.distributed.Scheduler", "opts":{}}'

    Unable to find image 'continuumio/miniconda3:latest' locally
    latest: Pulling from continuumio/miniconda3
    dc1f00a5d701: Already exists
    a7a9c78d89b2: Already exists
    44ac19016d77: Already exists
    Digest: sha256:977263e8d1e476972fddab1c75fe050dd3cd17626390e874448bd92721fd659b
    Status: Downloaded newer image for continuumio/miniconda3:latest
    /opt/conda/bin/python: Error while finding module specification for 'distributed.cli.dask_spec' (ModuleNotFoundError: No module named 'distributed')

If the ``dask.distributed`` scheduler fails to start, it's good to check that ``distributed`` is installed and the environment it is installed in has been activated. If you're having trouble running your Docker container on your Coiled cluster, feel free to :doc:`reach out to us <../support>` for help.

Install pip-installable packages
--------------------------------

If you have a package that is pip-installable, but not yet publicly available on PyPI or conda-forge, for example, you can use Dask's `PipInstall Worker Plugin <https://distributed.dask.org/en/latest/plugins.html?highlight=PipInstall#built-in-worker-plugins>`_ to pip install a set of packages. This is particularly useful for uploading modules that are still in development.

You can upload a public module in GitHub

.. code-block:: python

  from dask.distributed.diagnostics.plugin import PipInstall

  plugin = PipInstall(packages=["git+<github url>"])
  client.register_worker_plugin(plugin, name="<dependency name>")

If you want to install from a private repository you need to have a GitHub token set in your account by either having signed up with GitHub or by :doc:`adding your GitHub token to your profile <github_tokens>`. GitHub tokens are stored with Coiled and then used on the machine that's building the software environment; the token is not saved in the software environment.

.. code-block:: python

  from dask.distributed.diagnostics.plugin import PipInstall

  plugin = PipInstall(packages=["git+https://{GITHUB_TOKEN}@github.com/<repo>"])
  client.register_worker_plugin(plugin, name="<dependency name>")

.. note::

   Using the ``name=`` argument will allow you to call ``PipInstall`` more than once, otherwise you might see a message from workers like ``{'tls://10.4.1.170:38403': {'status': 'repeat'}``.
  
Upload a local directory
------------------------

Similar to the ``PipInstall`` Plugin, you can upload a local directory to your cluster by using the `UploadDirectory Nanny Plugin <https://distributed.dask.org/en/latest/plugins.html?highlight=PipInstall#built-in-nanny-plugins>`_.

You can upload a local directory from your machine to the cluster using:

.. code-block:: python

  from distributed.diagnostics.plugin import UploadDirectory

  client.register_worker_plugin(UploadDirectory("/path/to/directory"), nanny=True)

It's worth noting ``UploadDirectory`` will not install anything on its own. Ideally, you would package the code and directly use the ``PipInstall`` Worker Plugin mentioned above. However, if this is not possible you can write your own plugin for uploading and installation:

.. code-block::

    class InstallModulePlugin(UploadDirectory):
    """Use this plugging to upload a directory and install that directory in the workers."""
    def __init__(self, dir_path, module):
        """Initializes the plugin
        
        Arguments
        ---------
        dir_path: str, path to the directory you want to upload
        module: directory name
        """
        super().__init__(dir_path, update_path=True)
        self.module = module
        
    async def setup(self, nanny):
        await super().setup(nanny)
        
        import os
        import subprocess
        path_to_module = os.path.join(nanny.local_directory, self.module)
        
        # or whatever bash command to install package
        subprocess.call(["pip", "install", "-e", path_to_module]) 


    plugin = InstallModulePlugin("path_to_directory", "directory_name")
    client.register_worker_plugin(plugin, nanny=True)

Running post-installation commands
----------------------------------

In some cases, you may want to download additional files after installation. You can use the ``post_build`` keyword argument to run a command or add a path to a locally executable script. For example, when using the `spaCy <https://spacy.io/>`_ library, you will typically also want to download a trained pipeline after installing the package::

    python -m spacy download en_core_web_sm

You can do this with the ``post_build`` command, for example:

.. code:: python

    import coiled

    coiled.create_software_environment(
        name="spacy",
        conda=["coiled-runtime"],
        pip=["spacy"],
        post_build=["python -m spacy download en_core_web_sm"],
    )

The post build command will run after installation of any packages passed to ``conda`` and/or ``pip``.
