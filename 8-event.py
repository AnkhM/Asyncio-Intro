"""
Event allows for simpler synchronization by starting a task only when an event has been set/flagged
"""

import asyncio

async def waiter(event):
    print("waiting for the event to be set")
    await event.wait()
    print("Event has been set, continuing execution")

async def setter(event):
    await asyncio.sleep(2) # Simulate doing some work
    event.set()
    print("event has been set!")

async def main():
    event = asyncio.Event()
    await asyncio.gather(waiter(event), setter(event))

asyncio.run(main())