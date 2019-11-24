#!/usr/bin/env python3

'''
Timeouts
coroutine asyncio.wait_for(aw, timeout, *, loop=None)
Wait for the aw awaitable to complete with a timeout.
'''

import asyncio

from mylog import log

async def eternity():
    # Sleep for one hour
    await asyncio.sleep(3600)
    log('yay!')

async def main():
    log('main starts')
    # Wait for at most 1 second
    try:
        await asyncio.wait_for(eternity(), timeout=1.0)
    except asyncio.TimeoutError:
        log('timeout!')
    log('main finishes')

asyncio.run(main())

# Expected output:
#
#     timeout!
