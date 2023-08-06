Configuring GCP
===============

.. important::
    We recommend using the command-line setup option in the :doc:`gcp-cli`. If this option does not work for you, then continue with the steps below.

In this guide you will configure Coiled to run Dask computations entirely within
your own GCP account. You will first create a service account from your Google Cloud
account then configure your Coiled cloud account to use your Google Cloud account.

Before you start
~~~~~~~~~~~~~~~~

This guide assumes you have already `created your Coiled account <https://cloud.coiled.io/login>`_
and have a Google Cloud Platform (GCP) account. If you don't have a GCP account, you can
`sign up for a Free Tier account <https://cloud.google.com/free>`_.

You should also make sure you have the `gcloud CLI <https://cloud.google.com/sdk/docs/install>`_ installed and the following APIs enabled:

- `Artifact Registry <https://cloud.google.com/artifact-registry/docs/enable-service>`_
- Compute Engine (see `here <https://console.cloud.google.com/apis/library/compute.googleapis.com>`__ to enable from your console)
- BigQuery (see `here <https://console.cloud.google.com/apis/library/bigquery.googleapis.com>`__ to enable from your console)
- `Cloud Logging <https://cloud.google.com/logging/docs/api/enable-api>`_
- `Cloud Monitoring <https://cloud.google.com/monitoring/api/enable-api>`_
  
.. note::
    It can take a few minutes for these APIs to become active in your Google Cloud account.

Create a service account
~~~~~~~~~~~~~~~~~~~~~~~~

First, you will create a service account in your Google Cloud account with permissions to create clusters and the necessary infrastructure. Then you can :ref:`configure your Coiled cloud account <coiled-cloud-backend>`.

1. Sign in to the console
^^^^^^^^^^^^^^^^^^^^^^^^^
Sign in to the `Cloud Console <https://console.cloud.google.com/>`_.
See this `Google Cloud console reference <https://cloud.google.com/storage/docs/cloud-console>`_ for the different ways to access the Cloud console.

.. _gcp-iam-role:

2. Create an IAM custom role
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Coiled requires a limited set of IAM permissions to provision
infrastructure and compute resources in your GCP account. We recommend
creating a IAM custom role to align with the principle of least privilege
(see the `Google Cloud documentation on understanding IAM custom roles <https://cloud.google.com/iam/docs/understanding-custom-roles>`_).

.. important::
    This step requires the Role Administrator IAM role (``roles/iam.roleAdmin``)
    for a project or Organization Role Administrator IAM role (``roles/iam.organizationRoleAdmin``) for an organization
    (see the `Google Cloud documentation on required roles <https://cloud.google.com/iam/docs/creating-custom-roles#required-roles>`_).

Follow the steps in the Google Cloud documentation on
`creating a custom role <https://cloud.google.com/iam/docs/creating-custom-roles#creating_a_custom_role>`_.
Select the ``gcloud`` tab and follow the instructions using the gcloud CLI to
create a custom role using a YAML file.

Here’s an example YAML file you can customize with the specific permissions you’ll need.

.. dropdown:: Example IAM role for cluster service account
   :title: bg-white

   .. literalinclude:: ../../../../backends/policy/gcp-cluster-service-account.yaml
    :language: yaml

Then, use the ``gcloud`` command to create your custom IAM role in a
``PROJECT-ID`` of your choosing:

.. code-block:: text

   gcloud iam roles create coiled --project=<PROJECT-ID> --file=coiled.yaml

.. _create-service-account:

3. Create a service account
^^^^^^^^^^^^^^^^^^^^^^^^^^^
A service account provides the necessary identity and authentication for running Coiled.
In this step you will create a service account and grant the IAM role you created to this service account.
Follow the steps in the Google Cloud documentation on `creating a service account <https://cloud.google.com/iam/docs/creating-managing-service-accounts#creating>`_, selecting the ``Console`` tab.

.. important::
    This step requires the Service Account Admin (``roles/iam.serviceAccountAdmin``) IAM role on the project (see the `Google Cloud documentation on permissions <https://cloud.google.com/iam/docs/creating-managing-service-accounts#permissions>`_).

When you get to step 6 "Optional: Choose one or more IAM roles to grant to the service account on the project", choose the ``coiled`` IAM custom role you just created.

.. note::
    You can also bind the service account to the IAM custom role at any time using the 
    `Console <https://cloud.google.com/iam/docs/granting-changing-revoking-access#granting-console>`_ or `gcloud CLI command <https://cloud.google.com/iam/docs/granting-changing-revoking-access#granting-gcloud-manual>`_:

    .. code-block:: bash

        gcloud projects add-iam-policy-binding <PROJECT-ID> \
            --member=serviceAccount:<CLIENT-EMAIL> \
            --role=projects/<PROJECT-ID>/roles/coiled

4. Create a service account key
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Once you have a service account for working with
Coiled, you will need to create a JSON service account
key. Follow the steps in the Google Cloud documentation to
`create and manage a service account key <https://cloud.google.com/iam/docs/creating-managing-service-account-keys#creating_service_account_keys>`_.

After you create a JSON service account key, the key will be saved to your local
machine with a file name such as ``gcp-project-name-d9e9114d534e.json`` with
contents similar to:

.. code-block:: json

   {
     "type": "service_account",
     "project_id": "project-id",
     "private_key_id": "25a2715d43525970fe7c05529f03e44a9e6488b3",
     "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhki...asSSS5J4526eqmrkb1OA=\n-----END PRIVATE KEY-----\n",
     "client_email": "service-account-name@project-name.iam.gserviceaccount.com",
     "client_id": "102238688522576776582",
     "auth_uri": "https://accounts.google.com/o/oauth2/auth",
     "token_uri": "https://oauth2.googleapis.com/token",
     "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
     "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/service-account-name%40project-name.iam.gserviceaccount.com"
   }

Keep your JSON service account key handy since you will use it to later to :ref:`coiled-cloud-backend`.

.. _data_access_service_account:

5. Create a second service account for data access
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Coiled uses the service account that you created in the :ref:`previous step <create-service-account>` to create clusters and necessary infrastructure, and therefore requires a number of permissions including including network-related resources, firewall-related resources, and access to Cloud Storage.

Therefore, it is recommended you create a second service account for data access with more limited permissions to
only access the resources that you need while running your computation, such as access to BigQuery, Cloud Storage buckets and so on. Then, when you :ref:`configure your Coiled Cloud backend <coiled-cloud-backend>`, you can provide the URI of this service account for data access.

Follow the same steps in :ref:`gcp-iam-role` and :ref:`create-service-account` to create an additional IAM role named ``coiled_data`` and service account named ``coiled-data``.

This example YAML file for the IAM role has scope for submitting logs and accessing Google Storage. You can customize it with the specific permissions you'll need.

.. dropdown:: Example IAM role for data access service account
   :title: bg-white

   .. literalinclude:: ../../../../backends/policy/gcp-data-service-account.yaml
    :language: yaml

.. _gar:

6. Configure Google Artifact Registry
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you want to store the Docker containers for your software environments in
your own GCP account, Coiled stores them in the
`Google Artifact Registry (GAR) <https://cloud.google.com/artifact-registry>`_.
If you want to store your software environments in Docker Hub or another
external Docker registry, you can skip this step and configure the registry
settings when you :ref:`configure your Coiled Cloud backend <coiled-cloud-backend>`.

In this step, you'll enable the Google Artifact Registry (GAR) API, create a GAR
repository for Coiled, and create an IAM policy binding that grants limited
access to the service account for Coiled. Using this configuration, Coiled will
not have access to any other repositories in your GCP account, and Coiled does
not require admin-level permissions to enable APIs or create repositories.

To
`enable the Google Artifact Registry API <https://cloud.google.com/endpoints/docs/openapi/enable-api>`_,
run the following ``gcloud`` command in a terminal:

.. code-block:: bash

   gcloud services enable --project=<PROJECT_ID> artifactregistry.googleapis.com

`Create a GAR repository <https://cloud.google.com/artifact-registry/docs/manage-repos#create>`_
for Coiled to use by running the following command in a terminal. Note that the
repository must be named ``coiled`` exactly as shown, and that the location should
be one that we currently support: ``us-east1`` or ``us-central1``.
If you'd like to use a different region, please get in touch with
`Coiled Support <https://docs.coiled.io/user_guide/support.html>`_.

.. code-block:: bash

  gcloud artifacts repositories create coiled \
    --project=<PROJECT_ID> \
    --repository-format=docker \
    --location=<REGION>

Finally, grant access to the repository we just created:

.. code-block:: bash

   gcloud artifacts repositories add-iam-policy-binding coiled \
      --project=<PROJECT_ID> \
      --location=<REGION> \
      --member=serviceAccount:<CLIENT-EMAIL> \
      --role=roles/artifactregistry.repoAdmin

.. note::
   Ensure that the region specified in the ``location`` option is the same
   region you use when you
   :ref:`coiled-cloud-backend`.
   If you want to store software environments in multiple regions,
   then you can repeat these commands with the desired ``REGION``.

It can take a few minutes for the policy binding to propagate.
Keep this in mind if you quickly complete the next step and get
an error related to Google Artifact Registry.

.. _coiled-cloud-backend:

Configure your Coiled cloud account
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now you're ready to configure the cloud backend in your Coiled cloud account to
use your GCP account and GCP service account credentials.

1. Log in to your Coiled account
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

First, `log in to your Coiled account <https://cloud.coiled.io/login>`_.
In the navigation bar on the left, click on ``Setup``. Select
``Cloud Provider Configuration``, then click the ``Edit`` button:

.. figure:: images/cloud-backend-start.png
   :width: 100%

.. note::
   You can configure a different cloud backend for each Coiled account (i.e.,
   your personal/default account or your :doc:`Team account <teams>`). Be sure
   that you're configuring the correct account by switching accounts at the top
   of the left navigation bar in your Coiled dashboard if needed.

2. Select your cloud provider
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

On the ``Select Your Cloud Provider`` step, select the ``GCP`` option, then
click the ``Next`` button:

.. figure:: images/cloud-backend-provider-gcp.png
   :width: 100%

3. Network configuration
^^^^^^^^^^^^^^^^^^^^^^^^

On the ``Network Configuration`` step, select whether you would like
Coiled to automatically create new or manually use existing VPC and network resources
(see :doc:`tutorials/bring_your_own_network`):

.. figure:: images/cloud-backend-network.png
    :width: 100%

4. Configure GCP
^^^^^^^^^^^^^^^^

On the ``Configure GCP`` step, select the zone you want to use by
default (i.e., when a zone is not specified in the Coiled Python client). You
will need to add your JSON service account key file. Optionally, if you
created an :ref:`instance service account <data_access_service_account>`,
enter the service account email now. Then click the ``Next`` button:

.. figure:: images/cloud-backend-keys-gcp.png
   :width: 100%


.. _setup-gar:

5. Container registry
^^^^^^^^^^^^^^^^^^^^^

On the ``Container Registry`` step, select where you want to store Coiled
software environments, then click the ``Next`` button:

.. figure:: images/cloud-backend-registry-gcp.png
   :width: 100%

6. Review
^^^^^^^^^

Review the cloud backend provider options that you've configured, then click on
the ``Submit`` button:

.. figure:: images/cloud-backend-review-gcp.png
   :width: 100%

Next Steps
^^^^^^^^^^
Congratulations, Coiled is now configured to use your GCP account!

Follow the :doc:`Getting Started tutorial <getting_started>` to create a Coiled
cluster and run a computation. See :doc:`gcp_reference` for a more detailed
description and additional configuration options.