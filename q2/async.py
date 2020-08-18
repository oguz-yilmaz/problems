import asyncio

example_array = [1, 2, 3, 4]


async def print_async_array(arr):
    for idx, val in enumerate(arr):
        await dump_after(2**idx, val)


async def dump_after(delay, item):
    await asyncio.sleep(delay)
    print(item)


async def main():
    await print_async_array(example_array)

asyncio.run(main())
