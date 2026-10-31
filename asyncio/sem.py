import asyncio

async def access_resource(semaphore, resource_id):
    async with semaphore:
            # simulate a limited resource
            print(f"Accessing resource {resource_id}")
            await asyncio.sleep(2) #simulate work with resource
            print(f"Releasing resource {resource_id}\n")

async def main():
      semaphore = asyncio.Semaphore(2) #allow concurrent accesses
      await asyncio.gather(*(access_resource(semaphore, i) for i in range(5)))

asyncio.run(main())