=======================
Package Synchronization
=======================

.. important::

    Package sync is still in beta (see :ref:`known limitations below <package-sync-limitations>`).


Enabling package synchronization (package sync) is as simple as:

.. code-block:: python

    from coiled import Cluster

    with Cluster(package_sync=True):
        # dask work!
        pass


Package sync will then scan your local python environment, and replicate it to the cluster.

The Problem
-----------

By far the most common issue users encounter when running Dask in a true distributed fashion in the cloud, 
is that of environment **desynchronization**. When this happens, if you're lucky the error might be obvious. If you're 
unlucky you could be debugging strange error messages for hours, or worse have no errors but get results that are inconsistent!

Sometimes the errors only happen after hours of processing, leading to an incredibly frustrating experience.

So how does your environment get out of sync? Sometimes it's pretty straightforward, you pip installed something and forgot to run
``create_software_environment`` with your new package. 

Another example would be if you specify a conda  ``environment.yml`` file, for example:

.. code-block:: yaml

    channels:
    - conda-forge
    dependencies:
    - dask==2022.07.01
    - distributed==2022.07.01


On paper this looks pretty good. After all, we've pinned the exact versions the packages we need. Let's look at what this produces:

.. dropdown:: Full list

    .. code-block::

        bokeh==2.4.3      
        brotlipy==0.7.0          
        bzip2==1.0.8               
        ca-certificates==2022.6.15          
        certifi==2022.6.15     
        cffi==1.15.1          
        click==8.1.3         
        cloudpickle==2.1.0             
        cryptography==37.0.1          
        cytoolz==0.12.0
        dask==2022.7.1
        dask-core==2022.7.1
        distributed==2022.7.1
        freetype==2.10.4
        fsspec==2022.7.1
        heapdict==1.0.1
        idna==3.3
        jinja2==3.1.2
        jpeg==9e
        lcms2==2.12
        lerc==4.0.0
        libblas==3.9.0
        libcblas==3.9.0
        libcxx==14.0.6
        libdeflate==1.13
        libffi==3.4.2
        libgfortran==5.0.0.dev0
        libgfortran5==11.0.1.dev0
        liblapack==3.9.0
        libopenblas==0.3.21
        libpng==1.6.37
        libsqlite==3.39.2
        libtiff==4.4.0
        libwebp-base==1.2.4
        libxcb==1.13
        libzlib==1.2.12
        llvm-openmp==14.0.4
        locket==1.0.0
        lz4==4.0.0
        lz4-c==1.9.3
        markupsafe==2.1.1
        msgpack-python==1.0.4
        ncurses==6.3
        numpy==1.23.1
        openjpeg==2.5.0
        openssl==3.0.5
        packaging==21.3
        pandas==1.4.3
        partd==1.3.0
        pillow==9.2.0
        pip==22.2.2
        psutil==5.9.1
        pthread-stubs==0.4
        pycparser==2.21
        pyopenssl==22.0.0
        pyparsing==3.0.9
        pysocks==1.7.1
        python==3.10.5
        python-dateutil==2.8.2
        python_abi==3.10
        pytz==2022.2.1
        pyyaml==6.0
        readline==8.1.2
        setuptools==65.0.0
        six==1.16.0
        sortedcontainers==2.4.0
        sqlite==3.39.2
        tblib==1.7.0
        tk==8.6.12
        toolz==0.12.0
        tornado==6.1
        typing_extensions==4.3.0
        tzdata==2022b
        urllib3==1.26.11
        wheel==0.37.1
        xorg-libxau==1.0.9
        xorg-libxdmcp==1.1.3
        xz==5.2.6
        yaml==0.2.5
        zict==2.2.0
        zstd==1.5.2

Over 80 packages are installed by conda, and only two of them are pinned, which means any of them could change at any time.
We forgot to include python too so even the python version could change! We really only pinned the very tip of our environment iceberg.

So if you installed  this environment locally and created a Coiled software environment, then you'd probably only have a synchronized environment for a week or two
until one of these packages updated. 

The Solution
------------

For production, most people make a docker image and then use that in the cluster and their pipeline, which bypasses this issue. 
However, very few people enjoy developing in a docker image locally, especially on platforms where there's no native docker.

This is where package sync comes in. Instead of just looking at the tip of the iceberg, package sync works with your whole environment as-is
when you create a cluster!

Iterating on a feature and need to grab a new requirement to try something out? Great! Just pip/conda install it and start up a cluster, package 
sync has your back.

Package Sync Features
---------------------

Package Levels
==============

Critical Packages
#################

We maintain an internal list of packages we consider to be 'important' for a cluster, if you don't have these installed your cluster will never work

.. code-block:: text
    
    dask
    distributed
    tornado
    cloudpickle
    msgpack

We also ensure these packages match **exactly**. Even small mismatches here are likely to cause issues.

Unimportant Packages
####################

Both macOS and Windows have some packages that are only installed for them. For example Windows conda environments will often have
Windows API-related packages. Trying to install these on the Linux-based cluster would simply not work, so by default we ignore these.

Everything else
###############

By default, we take the version of your package locally and install it with ``<yourpackage>~=<version>``. We allow some wiggle room here
as being too strict cross-platform is often trouble, packages frequently have slightly different dependencies between platforms.

Path or Git dependencies
========================

Often you'll be working with packages installed locally via ``pip install -e <some-directory>``. Package sync will 
attempt to create a wheel of that package and sync it to the cluster, ensuring you're always running your latest changes in the cloud.

.. warning::
    This currently has the limitation that your package must work with ``pip wheel <package>``. If you have compiled dependencies,
    you must be running on the same platform as the cluster (64bit linux), we do not try to cross compile your package!

If you've installed a package from git with ``pip install git+ssh://git@github.com/dask/distributed`` for example, the same process will also occur.
The reason we build a wheel of git packages is to smooth issues with private git repos, building a wheel means we can keep your local credentials local,
instead of trying to get them onto the cluster!

.. warning::
    The compiled wheels are currently uploaded to a secure s3 bucket under the control of Coiled so they can be downloaded by your cluster.
    While this will change in the future, if this is undesirable we recommend not using package sync currently.

Package Sync for production
---------------------------

Package sync allows some fuzz between environments. This is to smooth over replication of environments between totally different OS's like linux and windows.
For a more strict experience where package sync tries to exactly match your local environment you can pass ``package_sync_strict``

.. code-block:: python

    Cluster(package_sync=True, package_sync_strict=True)


This is almost guaranteed to fail unless you match your client os/platform to the cluster. Currently this would be ubuntu/x86.

.. _package-sync-limitations:

Package Sync Limitations
------------------------

Unsolvable environments
=======================

Your environment needs to be consistent with what your package manager would accept as a valid environment.
For example

.. code-block:: text

    dask==2022.1.10
    distributed==2022.05.1

Pip will error out trying to install this environment, as will conda. This is because ``distributed`` has a pin on the matching ``dask`` version.

Virtual environments
====================

Using ``venv`` with package sync is much less tested than using conda. Here are some tips that may help during continued development:

- Install recent versions of ``pip`` and ``setuptools`` with ``pip install -U pip setuptools``
- Use ``pip install wheel``
- For pip installing packages that are not on PyPI, you may need the ``--use-pep517`` flag, for example:

.. code-block:: bash

    pip install git+https://github.com/dask/distributed.git --use-pep517


Packages you can't install locally
==================================

Sometimes you might be working with a package that can only be installed in the cluster environment, perhaps a gpu package.
Currently package sync does not allow you add an extra package just for the cluster.

Packages that have special build requirements
=============================================

If you have packages installed that don't have pre-built wheels available, and have requirements beyond what is included
in the standard ``build-essentials`` and ``python-dev`` ubuntu packages, you'll find package sync fails. If your package
is available in a conda repo we suggest using that instead.