===============================
Repeated cluster timeout errors
===============================

Sometimes creating a cluster can fail due to a connection timeout error, for example: 

.. code-block:: pytb

    OSError: Timed out trying to connect to tls://54.212.201.147:8786 after 5 s

This could be due to a port being blocked or due to using a very old version of Dask.
If you're using your own VPC (rather than one created by Coiled) or are restricting public
network access to your cluster, it's also possible something in your network is misconfigured.

First, check if default port 8786 is blocked by trying to load http://portquiz.net:8786 on your local machine. If that port is blocked on your local machine, see :ref:`blocked-ports` for instruction on how to work around this.

If you're using your own network functionality (see :doc:`../tutorials/bring_your_own_network`),
have configured a cluster firewall to only allow connections from certain CIDR blocks (see :ref:`cidr-block-ports`),
or are trying to connect to the scheduler on a private IP address (see :ref:`private-ip`),
you'll want to double-check your network configuration to make sure that your local
client is coming from the correct network/CIDR block and using the correct IP address.

If none of these apply and you're using a version of Dask that's over one year old,
see :ref:`troubleshoot-old-dask`, below.


.. _troubleshoot-old-dask:

Upgrading Dask
--------------

If you are using Dask version 2021.10.0, you may see this error repeated. 

.. dropdown:: Example of repeated errors

   .. code-block:: pytb

       tornado.application - ERROR - Exception in callback functools.partial(<bound
       method IOLoop._discard_future_result of <zmq.eventloop.ioloop.ZMQIOLoop object
       at 0x1334d13d0>>, <Task finished name='Task-337' coro=<Cluster._sync_cluster_info()
       done, defined at /Users/username/dev/distributed/distributed/deploy/cluster.py:104>
       exception=OSError('Timed out trying to connect to tls://54.212.201.147:8786 after 5 s')>)
       Traceback (most recent call last):
           File "/Users/username/dev/distributed/distributed/comm/tcp.py", line 398, in connect
           stream = await self.client.connect(
           File "/Users/username/dev/dask-playground/env/lib/python3.9/site-packages/tornado/tcpclient.py", line 288, in connect
           stream = await stream.start_tls(
       asyncio.exceptions.CancelledError

       During handling of the above exception, another exception occurred:

       Traceback (most recent call last):
           File "/Users/username/.pyenv/versions/3.9.1/lib/python3.9/asyncio/tasks.py", line 489, in wait_for
           fut.result()
       asyncio.exceptions.CancelledError

       The above exception was the direct cause of the following exception:

       Traceback (most recent call last):
           File "/Users/username/dev/distributed/distributed/comm/core.py", line 284, in connect
           comm = await asyncio.wait_for(
           File "/Users/username/.pyenv/versions/3.9.1/lib/python3.9/asyncio/tasks.py", line 491, in wait_for
           raise exceptions.TimeoutError() from exc
       asyncio.exceptions.TimeoutError

       The above exception was the direct cause of the following exception:

       Traceback (most recent call last):
           File "/Users/username/dev/dask-playground/env/lib/python3.9/site-packages/tornado/ioloop.py", line 741, in _run_callback
           ret = callback()
           File "/Users/username/dev/dask-playground/env/lib/python3.9/site-packages/tornado/ioloop.py", line 765, in _discard_future_result
           future.result()
           File "/Users/username/dev/distributed/distributed/deploy/cluster.py", line 105, in _sync_cluster_info
           await self.scheduler_comm.set_metadata(
           File "/Users/username/dev/distributed/distributed/core.py", line 785, in send_recv_from_rpc
           comm = await self.live_comm()
           File "/Users/username/dev/distributed/distributed/core.py", line 742, in live_comm
           comm = await connect(
           File "/Users/username/dev/distributed/distributed/comm/core.py", line 308, in connect
           raise OSError(
       OSError: Timed out trying to connect to tls://54.212.201.147:8786 after 5 s

    
.. note::
    The repeated error messages were caused when a periodic callback encountered an
    intermittent network connectivity issue and resulted in a frequently repeating
    error condition, as described in the following Dask
    `issue <https://github.com/dask/distributed/issues/5472>`_ and
    `resolution <https://github.com/dask/distributed/pull/5488>`_.

You can resolve the issue by upgrading to Dask versions >= 2021.11.0.

You'll want to update your local version of Dask, for example:

.. code-block::

    pip install dask distributed --upgrade

And also update your Coiled software environment:

.. code-block:: python

   coiled.create_software_environment(
       name="my-pip-env",
       pip=["dask>=2021.11.0", "distributed>=2021.11.0"],
   )

To ensure you're using the recommended versions of Dask and Coiled, you can also install ``coiled-runtime`` (see :ref:`coiled-runtime`)::

    pip install coiled-runtime
