import asyncio
import aiohttp


async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response.raise_for_status()
            return await response.json()


async def main():
    urls = [f"https://jsonplaceholder.typicode.com/posts/{i}" for i in range(1, 101)]
    conc = await asyncio.gather(
        *[fetch(url) for url in urls]
    )
    print(conc)


asyncio.run(main())


def calc():
    pass
