import asyncio

#define a coroutine that simulates a time consuming task
async def fetch_data(delay ,id):
    print("Fetching data.... id:", id)
    await asyncio.sleep(delay) #simulate an i/o operation with a sleep
    print("data fetched id:", id)
    return {"data": "data fetched", "id":id}


# define another coroutine that calls the first coroutine
async def main():
    print("Start of main coroutine")
    task1 = fetch_data(2,1)
    task2 = fetch_data(2,2)

    #await the fetch data coroutine
    result1 = await task1
    print(f"Received Result: {result1}")

    result2 = await task2
    print(f"Received Result: {result2}")

    print("End of main coroutine")

asyncio.run(main())