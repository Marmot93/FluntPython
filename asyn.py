import asyncio


async def agen(n, sleep=1.0):
    for i in range(n):
        await asyncio.sleep(sleep)
        yield i


async def main():
    l = [i ** 2 async for i in agen(10)]
    print(l)


main()
