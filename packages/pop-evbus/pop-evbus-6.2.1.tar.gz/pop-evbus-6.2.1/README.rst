=====
EVBUS
=====

An asynchronous message ingress system.
`evbus` is an app-merge component for larger projects.
Events are put on a broker queue.
A listener watches the broker queue and propagates events to configured ingress queues.

INSTALLATION
============

Install from pypi

.. code-block:: bash

    pip install pop-evbus

Install locally with testing libraries:

.. code-block:: bash

    $ git clone git@gitlab.com:vmware/idem/evbus.git
    $ pip install -e evbus -r evbus/requirements/test.in

Firing Events
=============

There are two functions that will put an event into the broker queue; `put` and `put_nowait`
The only difference between them is that `put` is asynchronous and `put_nowait` is synchronous.
Both accept a `routing_key`, `body`, and `profile`.

routing_key
-----------

This option is forwarded to the ingress plugins' `publish` functions.
Some message queues take a routing_key option themselves, some need to open a channel on the message queue
for the named routing_key.  It's up to the ingress plugins to implement this appropriately for the
message queue they wrap.

body
----

The event body is serialized by the evbus broker when it is put on the broker Queue.
The body can be any serializable object.
The serializer can be configured by setting `hub.serialize.PLUGIN` to the name of the plugin that should be used.

profile
-------

Configured profiles are formatted as follows:

.. code-block:: sls

    provider:
      profile_name:
          profile_data:

The `profile` parameter for the broker `put` and `put_nowait` functions specifies which profile_name should
be used for firing an event.
If no profile is specified, the profiles called "default" will be used.
There can be multiple providers with the same profile name,
the event will be forwarded to all providers that have a matching profile name.
A context (ctx) will be generated that will be sent to the appropriate ingress plugin's publish function
based on `profile`.


Full Example
------------

Asynchronous put:

.. code-block:: python

    async def my_func(hub):
        await hub.evbus.broker.put(
            routing_key="channel", body={"message": "event content"}, profile="default"
        )


Synchronous put:

.. code-block:: python

    def my_func(hub):
        hub.evbus.broker.put_nowait(
            routing_key="channel", body={"message": "event content"}, profile="default"
        )
