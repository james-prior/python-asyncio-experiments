#!/usr/bin/env python3

'''
valid uninteresting use of async

can await "awaitables" (only) in async function (i.e., coroutine)

The one benefit of this trivial example,
is that something else could be done while awaiting sleep.
There is nothing else to do while awaiting sleep,
which makes this example rather boring.
'''

import asyncio

from mylog import log

async def main():
    log('main: hello')
    await asyncio.sleep(1)
    log('main: world')

log('start')
asyncio.run(main())
log('end')
