=================
Managing clusters
=================

.. currentmodule:: coiled

You can use the Coiled Cloud web application to view currently running clusters and an overview of usage.

Clusters
--------

On the Dashboard page, you can see all clusters in your account that are currently running in addition to clusters that were recently closed. You can also use :meth:`coiled.list_clusters()` to systematically pull this information.

.. figure:: images/cloud-cluster-dashboard.png
    :width: 600px
    :align: center
    :alt: Table of clusters with columns for id, name, software environment, and a selectable button for logs.


You can also find an overview of your account usage on the Dashboard page, or pull this information using the :meth:`coiled.list_core_usage()`. One CPU hour is equivalent to one Coiled credit.


.. image:: images/cloud-cluster-usage.png
    :width: 600px
    :align: center
    :alt: A one by five table with columns for account core limit, account running cores, user core limit, user running cores, and credits remaining. Bar chart below of CPU Hours over time.

Analytics
---------

On the Analytics page you can see cluster activity for all team members, with a heat map of cluster compute usage. See :doc:`analytics` for more details.

.. figure:: images/cloud-analytics-usage.png
    :width: 600px
    :align: center


On this page you can also see a list of clusters and associated metrics including the cost and compute time.


.. figure:: images/cloud-analytics-clusters.png
    :width: 600px
    :align: center
