#!/usr/bin/env python3

'''
Example TCP echo server using async I/O.

The received text is echoed in upper case.

Each connection does the following one:
    receives up to 100 bytes.
    replies
    closes connection

This server handles multiple connections concurrently.
'''

import asyncio

from mylog import log

host, port = '127.0.0.1', 8888

async def handle_echo(reader, writer):
    name = f'handle_echo({(reader, writer)})'
    log(f'{name} starts')
    rx_message = await reader.read(100)
    addr = writer.get_extra_info('peername')

    log(f'Received {rx_message!r} from {addr!r}')

    tx_message = rx_message.upper()
    log(f'Send: {tx_message!r}')
    writer.write(tx_message)
    await writer.drain()

    log('Close the connection')
    writer.close()
    log(f'{name} finished')

async def main():
    log('main starts')

    server = await asyncio.start_server(handle_echo, host, port)
    log('main started server')

    addr = server.sockets[0].getsockname()
    log(f'Serving on {addr}')

    async with server:
        await server.serve_forever()
    log('main finishes')

asyncio.run(main())
