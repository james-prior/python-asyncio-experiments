#!/usr/bin/env python3

'''
Running Tasks Concurrently
awaitable asyncio.gather(*aws, loop=None, return_exceptions=False)
Run awaitable objects in the aws sequence concurrently.

# Expected output:
#
#     Task A: Compute factorial(2)...
#     Task B: Compute factorial(2)...
#     Task C: Compute factorial(2)...
#     Task A: factorial(2) = 2
#     Task B: Compute factorial(3)...
#     Task C: Compute factorial(3)...
#     Task B: factorial(3) = 6
#     Task C: Compute factorial(4)...
#     Task C: factorial(4) = 24
'''

import asyncio

from mylog import log

async def factorial(name, number):
    product = 1
    for i in range(2, number + 1):
        log(f'Task {name}: Compute factorial({i})...')
        await asyncio.sleep(1)
        product *= i
    log(f'Task {name}: factorial({number}) = {product}')
    return product

async def main():
    log('main starts')
    # Schedule three calls *concurrently*:
    result = await asyncio.gather(
        factorial('A', 2),
        factorial('B', 3),
        factorial('C', 4),
    )
    log(f'main finishes with result={result!r}')

asyncio.run(main())
