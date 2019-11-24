#!/usr/bin/env python3

'''
Python coroutines are awaitables
and therefore can be awaited from other coroutines.

There are no sleeps or blocking I/O, so this program runs quickly.
'''

import asyncio

from mylog import log

async def nested():
    return 42

async def main():
    log('main starts')

    # Nothing happens if we just call "nested()".
    # When we just call "nested()", it returns a coroutine object,
    # but does not execute the code inside it.
    log('main about to call nested() without awaiting it')
    foo = nested()
    log('main called nested() without awaiting it')
    log(f'Just got {foo} instead.')

    # Let's do it differently now and await it:
    log(await nested())  # will print "42".

    log('main finishes')

asyncio.run(main())
