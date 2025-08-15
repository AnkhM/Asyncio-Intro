import asyncio

# Define a corotuine that simulates a time-consuming task
async def fetch_data(delay): # -> Coroutine object
    print("Fetching data...")
    await asyncio.sleep(delay) # Simulate an I/O operation with a sleep
    print("Data fetched")
    return {"Data": "Some data"} # Return some data

# Define another coroutine that calls the 1st coroutine
async def main(): # -> Coroutine object
    print("Start of the main coroutine")
    task = fetch_data(2)
    # Await the fetch_data coroutine, pausing execution of main until fetch_data completes
    result = await task
    print(f"Received result: {result}")
    print("End of main coroutine")

# Run the main coroutine
asyncio.run(main())

