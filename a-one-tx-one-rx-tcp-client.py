#!/usr/bin/env python3

'''
Here is an example of a TCP client written using asyncio streams.

o connects to server
o sends message
o waits for reply (up to 100 bytes)
o then shows reply
o quits
'''

import asyncio

from mylog import log

host, port = '127.0.0.1', 8888

async def tcp_client(message):
    log(f'tcp_client({message}) starts')
    reader, writer = await asyncio.open_connection(host, port)

    log(f'Send: {message!r}')
    writer.write(message.encode())
    await writer.drain()

    data = await reader.read(100)
    log(f'Received: {data.decode()!r}')

    log('Close the connection')
    writer.close()
    await writer.wait_closed()
    log(f'tcp_client({message}) finishes')

asyncio.run(tcp_client('Hello World!'))
