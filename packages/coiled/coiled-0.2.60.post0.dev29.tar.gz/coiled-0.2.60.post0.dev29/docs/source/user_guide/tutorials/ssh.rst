How to SSH into your cluster
----------------------------

Coiled makes it easy to SSH directly into the schedulers or workers in your Coiled cluster. Coiled managed the authentication, using a unique keypair generated for each cluster.

First, you'll need to create a cluster with a port open for SSH. You can do this with ``allow_ssh=True``::

    # firewall doesn't restrict by IP, opens port 22
    coiled.Cluster(..., allow_ssh=True)

If you would also like to restrict by IP, you can use ``allow_ingress``::

    # only allow inbound connections from your public IP address
    coiled.Cluster(..., allow_ssh=True, allow_ingress_from="me")

    # restrict access to addresses in VPN/peered network
    coiled.Cluster(..., allow_ssh=True, allow_ingress_from="10.3.0.0/16")

.. note::
    The ``allow_ssh`` and ``allow_ingress`` arguments apply to the scheduler, all inbound connections to workers are blocked except connections from other machines in the cluster.

Then, you can connect using the CLI command. To connect to the scheduler:

.. code:: bash

   coiled cluster ssh 123  # cluster id
   coiled cluster ssh bob-73c2888d-f  # cluster name
   coiled cluster ssh bob-73c2888d-f --private  # connect to private IP address

Or to connect to a worker:

.. code:: bash

   coiled cluster ssh bob-73c2888d-f --worker any
   coiled cluster ssh bob-73c2888d-f --worker 10.6.58.234  # specify by IP
   coiled cluster ssh bob-73c2888d-f --worker bob-73c2888d-f-worker-115e5a1f13  # specify by name

When connecting to a worker, it uses the scheduler as jump, so you only need port 22 open on scheduler.

.. note::

    The CLI utility is a wrapper around OpenSSH CLI, so you'll need ``ssh`` and ``ssh-add`` runnable from the command line.



