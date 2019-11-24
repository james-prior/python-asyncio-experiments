#!/usr/bin/env python3

'''
Example TCP echo server using async I/O.

The received text is echoed in upper case.

Each connection lasts until it receives 'quit' or 'exit',
or is disconnected.
This server can handle multiple connections concurrently.
'''

import asyncio

from mylog import log

host, port = '127.0.0.1', 8888

async def handle_echo(reader, writer):
    addr = writer.get_extra_info('peername')
    name = f'echo with {addr!r}'
    log(f'{name} starts')

    while True:
        rx_message = await reader.readline()
        log(f'{name} Received {rx_message!r}')

        if not rx_message:
            log(f'{name} lost connection')
            break

        if rx_message.strip() in (b'quit', b'exit'):
            break

        tx_message = rx_message.upper()
        log(f'{name} Send {tx_message!r}')
        writer.write(tx_message)
        await writer.drain()

    log(f'{name} Close connection')
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
