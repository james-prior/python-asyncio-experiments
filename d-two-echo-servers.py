#!/usr/bin/env python3

'''
Two TCP echo servers
    server1 echoes received lines in upper case
    server2 echoes received lines in lower case

Each connection lasts until it receives 'quit' or 'exit'.
Each server can handle multiple connections concurrently.
'''

import asyncio

from mylog import log

host1, port1 = '127.0.0.1', 8888
host2, port2 = '127.0.0.1', 8889

async def handle_upper_echo(reader, writer):
    addr = writer.get_extra_info('peername')
    name = f'handle_upper_echo from {addr!r}'
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

async def handle_lower_echo(reader, writer):
    addr = writer.get_extra_info('peername')
    name = f'handle_lower_echo from {addr!r}'
    log(f'{name} starts')

    while True:
        rx_message = await reader.readline()
        log(f'{name} Received {rx_message!r}')

        if not rx_message:
            log(f'{name} lost connection')
            break

        if rx_message.strip() in (b'quit', b'exit'):
            break

        tx_message = rx_message.lower()
        log(f'{name} Send {tx_message!r}')
        writer.write(tx_message)
        await writer.drain()

    log(f'{name} Close connection')
    writer.close()
    log(f'{name} finished')

async def main():
    log('main starts')

    server1 = await asyncio.start_server(handle_upper_echo, host1, port1)
    log('main started server1')
    server2 = await asyncio.start_server(handle_lower_echo, host2, port2)
    log('main started server2')

    addr1 = server1.sockets[0].getsockname()
    log(f'main server1 on {addr1}')
    addr2 = server2.sockets[0].getsockname()
    log(f'main server2 on {addr2}')

    async with server1, server2:
        await asyncio.gather(
            server1.serve_forever(),
            server2.serve_forever(),
        )

    log('main finishes')

asyncio.run(main())
