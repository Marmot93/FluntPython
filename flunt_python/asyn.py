import asyncio, time

# async def agen(n, sleep=1.0):
#     for i in range(n):
#         await asyncio.sleep(sleep)
#         yield i
#
#
# async def main():
#     l = [i ** 2 async for i in agen(10)]
#     print(l)
#
#
# loop = asyncio.get_event_loop()
# task = loop.create_task(main())
# print(task)
# loop.run_until_complete(task)
# print(task)


# now = lambda: time.time()
#
#
# async def do_some_work(x):
#     print('Waiting: ', x)
#     return 'Done after {}s'.format(x)
#
#
# def callback(future):
#     print('Callback: ', future.result())
#
#
# start = now()
#
# coroutine = do_some_work(2)
# loop = asyncio.get_event_loop()
# task = asyncio.ensure_future(coroutine)
# task.add_done_callback(callback)
# loop.run_until_complete(task)
#
# print('TIME: ', now() - start)


# now = lambda: time.time()
#
# async def do_some_work(x):
#     print('Waiting: ', x)
#     await asyncio.sleep(x)
#     return 'Done after {}s'.format(x)
#
# start = now()
#
# coroutine1 = do_some_work(1)
# coroutine2 = do_some_work(2)
# coroutine3 = do_some_work(4)
#
# tasks = [
#     asyncio.ensure_future(coroutine1),
#     asyncio.ensure_future(coroutine2),
#     asyncio.ensure_future(coroutine3)
# ]
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(tasks))
#
# for task in tasks:
#     print('Task ret: ', task.result())
#
# print('TIME: ', now() - start)

import bs4, aiohttp


@asyncio.coroutine
def get(*args, **kwargs):
    response = yield from aiohttp.request('GET', *args, **kwargs)
    return (yield from response.read_and_close(decode=True))


def first_magnet(page):
    soup = bs4.BeautifulSoup(page)
    a = soup.find('a', title='Download this torrent using magnet')
    return a['href']


@asyncio.coroutine
def print_magnet(query):
    url = 'http://thepiratebay.se/search/{}/0/7/0'.format(query)
    page = yield from get(url, compress=True)
    magnet = first_magnet(page)
    print('{}: {}'.format(query, magnet))


distros = ['archlinux', 'ubuntu', 'debian']
loop = asyncio.get_event_loop()
f = asyncio.wait([print_magnet(d) for d in distros])
loop.run_until_complete(f)
