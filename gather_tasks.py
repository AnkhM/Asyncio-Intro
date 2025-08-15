import asyncio

async def fetch_data(id, sleep_time):
    print(f"Coroutine {id} starting to fetch data.")
    await asyncio.sleep(sleep_time)
    return {"id": id, "data": f"Sample data from coroutine {id}"}

async def main():
    # Run coroutines concurrently and gather their return values
    # gather() is not great at error handling and does not automatically cancel other coroutines if 1 of them fails
    results = await asyncio.gather(fetch_data(1,2), fetch_data(2,1), fetch_data(3,3))


    # Process the results
    for result in results:
        print(f"Received result: {result}")

asyncio.run(main())