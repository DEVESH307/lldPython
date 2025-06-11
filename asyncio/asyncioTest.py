# # 0. Async and Await Example(Original Code)
# import asyncio
# async def hello():
#     print("helloooooo")
#     await asyncio.sleep(1)
#     print('Hello World!')

# async def func1():
#     print("func1")


# async def main():
#     l = await asyncio.gather(hello(),
#     func1())
#     print(l)

# asyncio.run(main())


# # 1. Async Example(Modified Code)
# import asyncio
# import time
# async def hello():
#     time.sleep(1)  # This will block the event loop
#     print('Hello World!')

# asyncio.run(hello())
# # output: Hello World!


# # 2. Async Example(Modified Code)
# import asyncio
# import time
# async def hello():
#     time.sleep(1)  # This will block the event loop
#     print('Hello World!')

# def func1():
#     print("func1")

# async def main():
#     hello()
#     func1()

# asyncio.run(main())
# # output: RuntimeWarning: coroutine 'hello' was never awaited hello()
# # RuntimeWarning: Enable tracemalloc to get the object allocation traceback
# # func1


# # 2. Async and Await Example(Modified Code)
# import asyncio
# import time
# async def hello():
#     time.sleep(1)  # This will block the event loop
#     print('Hello World!')

# async def func1():
#     print("func1")

# async def main():
#     await hello()
#     await func1()

# asyncio.run(main())
# # output: Hello World!
# # func1

# 3. Async and Await Example(Modified Code)
# import asyncio
# import time
# async def hello():
#     print("helloooooo")
#     await asyncio.sleep(1)
#     print('Hello World!')

# async def func1():
#     print("func1")

# async def main():
#     l = await asyncio.gather(hello(), func1())
#     print(l)

# asyncio.run(main())
# # output: helloooooo
# # Hello World!
# # func1
# # [None, None]


import asyncio
import aiohttp
import aiofiles

async def download_file(url, filename):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                f = await aiofiles.open(filename, mode='wb')
                await f.write(await resp.read())
                await f.close()
                print(f"Downloaded: {filename}")
            else:
                print(f"Failed to download {url}, status: {resp.status}")

async def main():
    urls = [
        ("https://example.com", "example.html"),
        ("https://www.w3.org/TR/PNG/iso_8859-1.txt", "sample.txt"),
    ]
    
    tasks = [download_file(url, fname) for url, fname in urls]
    await asyncio.gather(*tasks)

# Run the async function
asyncio.run(main())
