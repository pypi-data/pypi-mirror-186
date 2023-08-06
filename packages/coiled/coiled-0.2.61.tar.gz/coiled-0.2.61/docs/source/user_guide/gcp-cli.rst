GCP Quickstart
~~~~~~~~~~~~~~

It's quick and easy to get started using Coiled in your own Google Cloud account.
This guide will cover the steps for getting started with Coiled
using the command-line interface, all from your terminal.

#. Install the Coiled Python library with::

    conda install -c conda-forge coiled-runtime python=3.9

   **or**::

    pip install coiled-runtime

#. Log in to your Coiled account::

    coiled login

#. Set up IAM

   If you would like to use the default options for network configuration and container registry, where Coiled creates a VPC in your account and uses Google Artifact Registry for storing your Python environments you can run::
    
       coiled setup gcp
    
   Otherwise, you can configure Coiled to use a custom network configuration (e.g. your pre-existing VPC) or a different container registry for your Python environment (e.g. Docker Hub)::

       coiled setup gcp --manual-final-setup

   After which you will be provided with the required access key and prompted to complete configuration in the Coiled web app at ``https://cloud.coiled.io/<your-account>/settings/setup/update-backend-options``.

   With your permission, this command will create the IAM roles and service accounts Coiled needs so you can create clusters in your GCP project. You will be prompted with an explanation at each step, so you can choose to say "yes" (or "no") at any point (see :doc:`gcp_configure` for more details).

#. Start your Dask cluster in the cloud (see :ref:`Running your computation <first-computation>`)::

    ipython
    > import coiled
    > cluster = coiled.Cluster(name="gcp-quickstart", n_workers=5)

If you don't already an GCP account and have more questions, see :ref:`Need a cloud provider account? <no-cloud-provider>`

Coiled makes it easy to deploy clusters in a way that's secure by default.
If you have questions about how we handle security, see our documentation about :doc:`security` (or :doc:`talk to us <support>`!).