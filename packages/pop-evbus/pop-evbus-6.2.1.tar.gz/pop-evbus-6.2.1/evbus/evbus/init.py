import asyncio
import sys
from typing import Any
from typing import Dict
from typing import List

STOP_ITERATION = object()


def __init__(hub):
    hub.evbus.STARTED = False
    for dyne in ("acct", "ingress", "output", "serial", "match"):
        hub.pop.sub.add(dyne_name=dyne)


async def start(hub, contexts: Dict[str, List[Dict[str, Any]]]):
    hub.log.debug("Starting event bus")
    hub.evbus.STARTED = True

    # Initialize the queue in the current loop
    bus: asyncio.Queue = await hub.evbus.broker.init()

    while True:
        item = await bus.get()
        event = item[1]
        if event is STOP_ITERATION:
            hub.log.info("Event bus was forced to stop")
            return
        await hub.evbus.broker.propagate(contexts=contexts, event=event)


async def stop(hub):
    """
    Stop the event bus
    """
    hub.log.debug("Stopping the event bus")
    bus: asyncio.PriorityQueue = hub.evbus.BUS
    # This has to be the highest priority, so that it is processed in the last
    bus.put_nowait((sys.maxsize, STOP_ITERATION))


async def join(hub):
    while not hub.evbus.STARTED:
        await hub.pop.loop.sleep(0)
