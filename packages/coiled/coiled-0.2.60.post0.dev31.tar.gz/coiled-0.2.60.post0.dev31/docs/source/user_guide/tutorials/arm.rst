Using ARM on Coiled
===================

Coiled supports ARM (Graviton) instance types on AWS.

We found that for some workloads, ARM is significantly faster and cheaper. We don't yet know how to predict whether a specific workload will be better on ARM, but we encourage you to try for yourself!

Limitations
-----------

Coiled offers a variety of ways do get the Python packages you need installed on your cluster:

#. You can use :meth:`coiled.create_software_environment` and specify a list of packages to install with pip or conda.
#. You can use package sync to have us install packages based on what you have in your local environment.
#. You can use a pre-built Docker image.

Currently only (3) is supported for ARM instances—support for other options is on our TODO list.

You can either build your own Docker image (harder) or you can use the coiled-runtime 0.1.1 image which is already built for both x86 and ARM.

Starting a cluster
------------------

If coiled-runtime has the packages you need, then it's easiest to use that on the cluster. You can first install it locally, using mamba to create your Python environment:

.. code-block:: bash

    mamba create -n runtime-011 python=3.10 coiled-runtime=0.1.1
    mamba activate runtime-011


Then, wherever you run Python, you can create your cluster:

.. code-block:: python

    import coiled

    cluster = coiled.Cluster(
        # ARM instance types for scheduler and workers
        scheduler_vm_types=["t4g.large"],
        worker_vm_types=["c7g.xlarge"],
        n_workers=10,
        # no software env specified, so will match coiled-runtime version, equivalent to
        # software='coiled/coiled-runtime-0-1-1-py310'
    )


You can select instance types based on the recommendations above, and request as many workers as you want!

If coiled-runtime doesn't have what you need, build your multi-arch Docker image (see :ref:`arm-custom-docker` below), create a Coiled software environment from that image, and then use that on your cluster (see :ref:`custom-docker`).

.. _arm-custom-docker:

Using a custom Docker image
---------------------------

You can use GitHub Actions to build your own multi-arch (x86 and ARM) Docker image (see this `example yaml file <https://github.com/coiled/coiled-runtime/blob/e9aa85937911ed477f4294ae7388d96d6d0153fc/.github/workflows/software-environments-stable.yml#L47>`_).

Locally, you can build multi-arch images like this:

.. code-block:: bash

    docker buildx build --platform linux/arm64,linux/amd64 \
    -t <your-image-name>:latest --push .

You can then upload your local image to wherever you usually store Docker images (e.g. Docker Hub or Amazon ECR) and create a Coiled Python environment using this image (see :ref:`custom-docker` for instructions).

Instance types
--------------

For common Intel instance types you might be using already, there's a roughly equivalent ARM instance type you could try instead.

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Intel
     - ARM
     - Description
   * - t3
     - t4g
     - burstable (best for interactive non-compute intensive work)
   * - m6i/m6id
     - m6g/m6gd
     - non-burstable balanced compute/memory (sensible default for common workloads)
   * - r6i/r6id
     - r6g/r6gd
     - memory-optimized (higher ratio of memory to vCPUs)
   * - c6i
     - c7g
     - compute-optimized (higher ratio of vCPUs to memory)

For instances with/without the "d" suffix, "d" means NVMe (Non-Volatile Memory Express), i.e. faster disk, instead of EBS (Amazon Elastic Block Store), i.e. slower disk.

If you're currently using m6i instances, we'd also suggest trying c7g instances the next size up. For example, instead of m6i.large, try the same number of c7g.xlarge instances.

.. admonition:: Explanation

    Only the c7g family has the newest generation Graviton3 processors, and these are significantly better than previous generations. But c7g is "compute optimized", so it has less memory per instance than equivalent m6i. Using next size up with c7g means you'll have as much memory per instance. Cost per instance/hour is higher, but if your workload completes in significantly less time—which we've seen for some workloads—your total cost will still be lower.

