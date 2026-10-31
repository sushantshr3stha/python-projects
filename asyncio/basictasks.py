import asyncio

async def fetch_data(id, sleep_time):
    print(f"Coroutine {id} starting to fetch data ")
    await asyncio.sleep(sleep_time)
    return {"id":id, "data": f"Sample data from coroutine {id}"}

async def main():


    # task1 = asyncio.create_task(fetch_data(1,3))
    # task2 = asyncio.create_task(fetch_data(2,2))
    # task3 =  asyncio.create_task(fetch_data(3,4))

    # result1 = await task1
    # # print(f"Recieved result {result1}")

    # result2 = await task2
    # # print(f"Recieved result {result2}")

    # result3 = await task3
    # # print(f"Recieved result {result3}")

    # print(result1,result2,result3)

    # results = await asyncio.gather(fetch_data(1,2), fetch_data(2,3), fetch_data(3,3)) #gather doesn't provide error handling

    # for result in results:
    #     print(f"Results: {result}")
    tasks = []
    async with asyncio.TaskGroup() as tg: #TaskGroup have builtin error handling
        for i, sleep_time in enumerate([2,3,1], start=1):
            task = tg.create_task(fetch_data(i, sleep_time))
            tasks.append(task)

# after the TaskGroup block all the task have been completed

    results = [task.result() for task in tasks]
    for result in results:
        print(f"Got results {result}")

asyncio.run(main())