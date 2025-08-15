import asyncio

# Define a corotuine that simulates a time-consuming task
async def fetch_data(delay, id): # -> Coroutine object
    print("Fetching data...id:", id)
    await asyncio.sleep(delay) # Simulate an I/O operation with a sleep
    print("Data fetched, id:", id)
    return {"Data": "Some data", "id": id} # Return some data

# Define another coroutine that calls the 1st coroutine
async def main(): # -> Coroutine object
    print("Start of the main coroutine")
    task1 = fetch_data(2, 1)
    task2 = fetch_data(2,2)
    # Await the fetch_data coroutine, pausing execution of main until fetch_data completes
    result1 = await task1
    print(f"Received result: {result1}")
    result2 = await task2
    print(f"Received result: {result2}")
    print("End of main coroutine")

# Run the main coroutine
asyncio.run(main())

