import asyncio

total = 100


async def start_race(total):
    archilles = 0
    tortoise = 50
    while True:
        await render(archilles, tortoise)
        tortoise = tortoise + (total - tortoise)/3
        archilles = archilles + (tortoise-archilles)/2


async def render(archilles, tortoise):
    await asyncio.sleep(1)
    print("Archilles at => ", archilles, "Tortoise at => ", tortoise)
    print("---------------------------------------------------------")


async def main():
    await start_race(total)

asyncio.run(main())
