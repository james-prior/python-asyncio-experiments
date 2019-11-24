#!/usr/bin/env python3

'''
Run two invocations of say_after coroutines concurrently.
(As opposed to running them sequentially.)

The asyncio.create_task() function can be used
to run coroutines concurrently as asyncio Tasks.

asyncio.create_task creates and starts tasks immediately.
'''

import asyncio

from mylog import log

async def say_after(delay, what):
    log(f'say_after({delay}, {what}) starts {delay} second delay')
    await asyncio.sleep(delay)
    log(what)

async def main():
    log('main starts')

    # asyncio.create_task creates and starts task1 immediately
    task1 = asyncio.create_task(
        say_after(1, 'hello'))
    log('task1 created')

    # asyncio.create_task creates and starts task2 immediately
    task2 = asyncio.create_task(
        say_after(2, 'world'))
    log('task2 created')

    # Wait until both tasks are completed
    await task1 
    log('await task1 finished')
    await task2
    log('await task2 finished')

    log('main finishes')

asyncio.run(main())
