#!/usr/bin/env python3

'''
Awaiting on a coroutine.

Print “hello” after waiting for 1 second,
and then print “world” after waiting for another 2 seconds.

Note that waits are sequential.
'''

import asyncio

from mylog import log

async def say_after(delay, what):
    await asyncio.sleep(delay)
    log(what)

async def main():
    log('main starts')

    await say_after(1, 'hello')
    await say_after(2, 'world')

    log('main finishes')

asyncio.run(main())
