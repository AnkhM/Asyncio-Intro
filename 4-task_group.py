import asyncio

async def fetch_data(id, sleep_time):
    print(f"Coroutine {id} starting to fetch data.")
    await asyncio.sleep(sleep_time)
    return {"id": id, "data": f"Sa,ple data from coroutine {id}"}

async def main():
    tasks = []
    # TaskGroup() is better for error handling as it cancels all tasks if 1 has an error
    async with asyncio.TaskGroup() as tg:
        for i, sleep_time in enumerate([2,1,3], start=1):
            task = tg.create_task(fetch_data(i, sleep_time))
            tasks.append(task)
    
    # After the Task Group block, all tasks have completed
    results = [task.result() for task in tasks]

    for result in results:
        print(f"Received result: {result}")