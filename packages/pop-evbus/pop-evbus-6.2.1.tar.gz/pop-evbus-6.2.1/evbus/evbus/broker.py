import asyncio
import dataclasses
import queue
import uuid
from typing import Any
from typing import Dict
from typing import List

import dict_tools.data as data


def __init__(hub):
    # Start off with a synchronous queue
    hub.evbus.SERIAL_PLUGIN = "json"
    hub.evbus.BUS = queue.Queue()


@dataclasses.dataclass
class Event:
    profile: str
    body: bytes


async def get(hub):
    bus: asyncio.PriorityQueue = await hub.evbus.broker.init()
    queue_item = await bus.get()
    return queue_item[1]


async def init(hub):
    """
    Initialize the event bus queue in the current loop
    """
    # Once we are running in the context of asyncio, replace the synchronous queue with an async queue
    if isinstance(hub.evbus.BUS, queue.Queue):
        new_bus = asyncio.PriorityQueue()
        while not hub.evbus.BUS.empty():
            queue_item = hub.evbus.BUS.get()
            if isinstance(queue_item, tuple):
                new_bus.put_nowait(queue_item)
            else:
                # If the item exists in original synchronous queue without priority
                # Add the priority before putting into priority queue in this conversion
                new_bus.put_nowait((_random_priority(), queue_item))

        hub.evbus.BUS = new_bus
    return hub.evbus.BUS


async def put(hub, body: str, profile: str = "default"):
    """
    Put an event on the bus as a single data class
    :param hub:
    :param body: The message body that will be serialized and put on the bus
    :param profile: The ctx profile name that should be used for this message
    :param serial_plugin: The pop-serial plugin used to serialize data
    """
    bus: asyncio.PriorityQueue = await hub.evbus.broker.init()
    await bus.put(_create_queue_item(hub, body, profile))


def put_nowait(hub, body: str, profile: str = "default"):
    """
    Put an event on the bus as a single data class
    """

    if not isinstance(hub.evbus.BUS, asyncio.PriorityQueue):
        # The event bus init may not complete before items starts going into the queue
        # All events before init will be inserted into regular queue.
        # init converts synchronous queue into asynchronous queue (priority queue)
        serialized: bytes = hub.serial[hub.evbus.SERIAL_PLUGIN].dump(body)
        hub.evbus.BUS.put_nowait(Event(body=serialized, profile=profile))
    else:
        bus: asyncio.PriorityQueue = hub.evbus.BUS
        bus.put_nowait(_create_queue_item(hub, body, profile))


async def propagate(
    hub,
    contexts: Dict[str, List[Dict[str, Any]]],
    event: Event,
):
    """
    Publish an event to all the ingress queues
    """
    match_plugin = contexts.get("match_plugin", hub.match.PLUGIN)
    coros = []
    for plugin in hub.ingress:
        # get a list of allowed acct plugins for this publisher
        acct_plugins = getattr(plugin, "ACCT", [])
        if not acct_plugins:
            raise NotImplementedError(
                f"No acct providers specified for ingress.{plugin.name}, specify ACCT providers.  I.E.\n"
                f"def __init__(hub):\n"
                f"    hub.ingress.{plugin.name}.ACCT = ['acceptable_acct_providers']\n"
            )

        for acct_plugin in acct_plugins:
            provider = contexts.get(acct_plugin, {})
            for profile in provider:
                for name in profile:
                    # Treat the profile name as a pattern, and see if the event profile name matches
                    if hub.match[match_plugin].find(name=event.profile, pattern=name):
                        ctx = data.NamespaceDict(acct=profile[name])
                        # co-routines cannot be awaited more than once, but tasks can be
                        # We need plugin and event metadata so that we can send the failure to error callback handler
                        publish_task = asyncio.create_task(
                            hub.evbus.broker.wrap(
                                getattr(plugin, "__name__", None),
                                event,
                                contexts,
                                coro=plugin.publish(ctx=ctx, body=event.body),
                            )
                        )
                        coros.append(publish_task)

        await asyncio.gather(*coros)


async def wrap(hub, plugin_name, event, contexts, coro):
    try:
        return await coro
    except Exception as e:
        # Log all failures, in case log messages are being sent to a queue the error message will be formatted
        hub.log.error(
            f"Event failed to propagate on plugin {plugin_name} with profile {event.profile}: {e.__class__.__name__}: {e}"
        )
        if hub.OPT.evbus.error_callback_ref:
            hub.log.trace(
                f"The error from {plugin_name} is being sent to error callback handler {hub.OPT.evbus.error_callback_ref}"
            )
            error_data = {
                "exception": e,
                "plugin": plugin_name,
                "profile": event.profile,
                "body": event.body,
                "context": contexts,
            }
            await hub.pop.loop.wrap(hub[hub.OPT.evbus.error_callback_ref], error_data)


def _create_queue_item(hub, body: str, profile: str = "default") -> tuple:
    serialized: bytes = hub.serial[hub.evbus.SERIAL_PLUGIN].dump(body)
    return _random_priority(), Event(body=serialized, profile=profile)


def _random_priority() -> int:
    # Using uuid4 so that priority value collision chances are very less.
    # If used a random number and there is a collision,
    #   - It would fall back on comparing Event object
    #   - Event has no comparator and would fail with TypeError
    #       - Error: '<' not supported between instances of 'Event' and 'Event'
    #       - There is no comparator for Event dataclass
    #
    # Store everything as negative, as it is using min-heap
    # CAUTION: DO NOT use this method for storing terminal (STOP_ITERATION) event.
    # The terminal event should be the highest number in the heap, so it is fetched last
    return -1 * int(uuid.uuid4())
