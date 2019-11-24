#!/usr/bin/env python3

'''
Simplification of
3-concurrent-tasks-waiting-using-create-task-await.py
by using async.gather
to create, start, and await multiple tasks.

Run two invocations of say_after coroutines concurrently
(as opposed to running them sequentially.)
'''

import asyncio

from mylog import log

async def say_after(delay, what):
    log(f'say_after({delay}, {what}) starts {delay} second delay')
    await asyncio.sleep(delay)
    log(what)

async def main():
    log('main starts')
    # Schedule two calls *concurrently*:
    result = await asyncio.gather(
        say_after(1, 'hello'),
        say_after(2, 'world'),
    )
    log(f'main finishes with result={result!r}')

asyncio.run(main())
