=====
Teams
=====

Coiled helps individuals and teams manage their resources, control costs, and
collaborate with one another. Team members can share resources, track usage, and consolidate billing
with anyone else on the same account.

Users and accounts
------------------
When you `sign up for Coiled <https://cloud.coiled.io/login>`_, an account is
automatically created for your user, and the name of the account is the same as
your username. For example, if you sign up with the username ``awesome-dev``,
then the ``awesome-dev`` user is automatically added to an account also named
``awesome-dev``.  

If you want to work with a team of two or more users, you can either:

1. Add other users to your existing account by using the Team page at
   ``cloud.coiled.io/<YOUR-ACCOUNT-NAME>/team``

2. Reach out to us at support@coiled.io to create an additional account to use
   for your team such as ``cloud.coiled.io/<YOUR-COMPANY-NAME>/team``

Taking the screenshot below as an example, note that this user Kris (seen in the
avatar on the top right) is viewing the Team page of the Coiled account (seen in
the dropdown on the left).

.. image:: images/team-management.png
    :width: 100%
    :alt: Coiled team page with three users

Sharing resources
-----------------

You can create clusters, software environments, and other resources from any account of which you are a member.

You can see all accounts of which you are a member from the Coiled web application. Select your avatar from the top right, then select Profile. The Accounts section is at the bottom of the page. In the example below, user ``sarah-johnson`` is a user on both the ``sarah-johnson`` account and the ``sarahs-team`` account.

.. figure:: images/team-account.png
    :scale: 75%
    :align: center
    :alt: This user has access to the sarah-johnson and the sarahs-team accounts.

You can change your default account by using the ``coiled login`` CLI tool (see :ref:`coiled-login-cli`), which will set the account in your local Coiled configuration file ``~/.config/dask/coiled.yaml`` (see :doc:`configuration`).

.. code-block::

    coiled login --account <your-team-account>

Or, you can specify your account by using the ``account`` keyword argument commonly accepted in :doc:`API commands <api>`. For example, if ``sarah-johnson`` wants to create a cluster in ``sarahs-team``:

.. code-block:: python

   import coiled

   cluster = coiled.Cluster(n_workers=5, account="sarahs-team")

Or create a software environment accessible to other team members:

.. code-block:: python

   import coiled

   coiled.create_software_environment(
       name="sarahs-team/my-pip-env",
       pip=["dask[complete]", "xarray==0.15.1", "numba"],
   )

.. note::
    Once you are added to an account, you can use the cloud provider resources and credentials that have already been set up for your team. Similarly, any tokens you've created will work for any account to which you belong (there is no need to create a new token).

Tracking usage
--------------

You can see usage for a single account on the Dashboard page:

.. figure:: images/cloud-cluster-usage.png
    :width: 600px
    :align: center
    :alt: A one by five table with columns for account core limit, account running cores, user core limit, user running cores, and credits remaining. Bar chart below of CPU Hours over time.

Additionally, on the Billing page (only visible to account admins) you can see more detailed information on account usage such as your credit balance, credits used, and percentage of free credits used.

.. figure:: images/cloud-billing-free.png
    :width: 600px
    :align: center
    :alt: Monthly billing table available for PAYG customers. 

If you have added a credit card to your account, you will also have visibility into your Coiled bill for the month:

.. figure:: images/cloud-billing-payg.png
    :width: 600px
    :align: center
    :alt: Monthly billing table available for PAYG customers. 

If your usage stays below the amount of free credits, then this value will always show $0 since you don't have to pay Coiled anything.

Managing resources
------------------

Administrators for a Coiled team can set resource limits for team members including:

#. **Team-level vCPUs.** The number of virtual CPUs that can be running for a team at a given time. If you'd like to change this setting, please reach out to us at support@coiled.io.
#. **User-level vCPUs.** The number of virtual CPUs that can be running in a user's account at a given time. You can set this limit for any user on your team from the Team page.
#. **Monthly spend.** You can set this from the billing page, see :ref:`set-spend-limit` below.

.. _set-spend-limit:

Setting a spend limit
^^^^^^^^^^^^^^^^^^^^^

.. important::
   This spend limit only applies to your Coiled bill, not the bill you receive from your cloud provider.

By default, your Coiled account doesn't have a spend limit. You can set a monthly spend limit to ensure your Coiled bill will not exceed a maximum specified value. This limit will be enforced once you have used up your free Coiled credits.

.. figure:: images/cloud-billing-spend-limit.png
    :width: 500px
    :align: center
    :alt: Setting spend limit

Once the spend limit is reached, users will not be able to create new clusters and running clusters will be automatically shut down. You can uncheck **Shut down running clusters if spend limit reached** to not impact already running clusters.
