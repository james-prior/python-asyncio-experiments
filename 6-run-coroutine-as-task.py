#!/usr/bin/env python3

'''
Tasks are used to schedule coroutines concurrently.

When a coroutine is wrapped into a Task with functions
like asyncio.create_task()
the coroutine is automatically scheduled to run soon:

There are no sleeps or blocking I/O, so this program runs quickly.

This program has only one task.
I.e., there is no other task to run concurrently with,
so by itself, this program is not do something that
its non-task predecessors did.

In showing how to run a coroutine as a task,
it lays the foundation for running multiple
coroutine currently by running them as tasks.
'''

import asyncio

from mylog import log

async def nested():
    return 42

async def main():
    log('main starts')

    # Schedule nested() to run soon concurrently with "main()".
    task = asyncio.create_task(nested())
    log(f'main just created task {task}')

    # "task" can now be used to cancel "nested()", or
    # can simply be awaited to wait until it is complete:

    log(f'result of await task is {await task}')
    log('main finishes')

asyncio.run(main())
