"""
Lock is used to prevent multiple coroutines from accessing the shared resource at the same time.
Otherwise, the couroutines would modify the same resource at the same time and lead to weird results or errors.
That is why we lock off the resource so only 1 coroutine runs at a time.
"""

import asyncio

# A shared variable (could also be a database, table, file, etc.)
shared_resource = 0

# An asyncio Lock that allow us to synchronize execution of coroutines
lock = asyncio.Lock()

async def modify_shared_resource():
    global shared_resource
    async with lock:
        # Critical section starts
        print(f"Resource before modification: {shared_resource}")
        shared_resource += 1    # Modify the shared resource
        await asyncio.sleep(1)  # Simulate an IO operation
        print(f"Resource after modification: {shared_resource}")
        # Critical sectiond ends

async def main():
    # Gather, which usually runs tasks at the same time, now runs these tasks 1 after the other because of the lock
    await asyncio.gather(*(modify_shared_resource() for _ in range(5)))

