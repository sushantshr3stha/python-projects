import asyncio

# a shared variable

shared_resuorce = 0

# a asyncio lock
lock = asyncio.Lock()

async def modify_shared_resource():
    global shared_resuorce
    async with lock:
        # critical session starts
        print(f"Resource before modification: {shared_resuorce}")
        shared_resuorce +=1 #modify the shared resource
        await asyncio.sleep(2) #simulate an io operation
        print(f"Resource after modification: {shared_resuorce}")
        # critical section ends

async def main():
    await asyncio.gather(*(modify_shared_resource() for _ in range(5)))

asyncio.run(main())