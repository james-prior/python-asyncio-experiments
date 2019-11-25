#!/usr/bin/env python3

'''
Two TCP echo servers
    server1 echoes received lines in upper case
    server2 echoes received lines in lower case

Each connection lasts until it receives 'quit' or 'exit'.
Each server can handle multiple connections concurrently.
'''

import fcntl
import os
import sys
import asyncio

from mylog import log

host1, port1 = '127.0.0.1', 8888
host2, port2 = '127.0.0.1', 8889

global_writer = None


async def handle_upper_echo(reader, writer):
    global global_writer

    global_writer = writer
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

    global_writer = None
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


def process_stdin():
    s = sys.stdin.read()
    if global_writer:
        global_writer.write(f'from stdin: {s!r}\n'.encode('ascii'))
        # await global_writer.drain()
    log(f'process_stdin: read {len(s)} bytes: {s!r}')


def initialize_listening_to_stdin():
    # set sys.stdin non-blocking
    orig_fl = fcntl.fcntl(sys.stdin, fcntl.F_GETFL)
    fcntl.fcntl(sys.stdin, fcntl.F_SETFL, orig_fl | os.O_NONBLOCK)

    loop = asyncio.get_running_loop()
    log(f'initialize_listening_to_stdin loop={loop}')

    loop.add_reader(sys.stdin, process_stdin)


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

    initialize_listening_to_stdin()

    async with server1, server2:
        await asyncio.gather(
            server1.serve_forever(),
            server2.serve_forever(),
        )

    log('main finishes')


asyncio.run(main())
