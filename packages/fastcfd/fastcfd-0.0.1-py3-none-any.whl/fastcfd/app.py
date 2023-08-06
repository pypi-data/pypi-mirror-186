#!/usr/bin/env python3
import asyncio
import os

import aiohttp
import codefast as cf
import fire
import regex


async def startall(port: int):
    t1 = asyncio.create_task(start_cloudflared(port))
    t2 = asyncio.create_task(sync_tunnel_info(port))
    t3 = asyncio.create_task(collect_err())
    await asyncio.gather(t2, t1, t3)


log_path = '/tmp/cloudflare_tunnel_{}.log'.format(cf.random_string(7))


async def _start_bin(bin_name: str, *args):
    pwd = os.path.dirname(os.path.abspath(__file__))
    bin_cmd = os.path.join(pwd, 'bins', bin_name)
    cf.info(f'starting {bin_cmd}')
    file_handler = open(log_path, 'w')
    proc = await asyncio.create_subprocess_exec(bin_cmd,
                                                *args,
                                                stdout=file_handler,
                                                stderr=file_handler)
    cf.info('process [ {} ] started, pid is [ {} ]'.format(bin_name, proc.pid))
    stdout, stderr = await proc.communicate()


async def get_tunnel_url() -> str:
    with open(log_path) as f:
        return regex.findall(r'(https:.*trycloudflare\.com)', f.read())[-1]


async def collect_err():
    while True:
        with open(log_path) as f:
            for line in f.readlines():
                if 'ERR' in line:
                    cf.error(line)
        await asyncio.sleep(10)


async def get_key(port: int) -> str:
    """Get tunnel key"""
    proc = await asyncio.create_subprocess_exec('hostname',
                                                stdout=asyncio.subprocess.PIPE)
    stdout, stderr = await proc.communicate()
    hostname = stdout.decode().strip()
    return '-'.join(['tunnel', hostname, str(port)])


async def sync_tunnel_info(port: int):
    await asyncio.sleep(5)
    async with aiohttp.ClientSession() as session:
        while True:
            try:
                tunnel_name = await get_key(port)
                tunnel_url = await get_tunnel_url()
                payload = {'key': tunnel_name, 'value': tunnel_url}
                cf.info(payload)
                async with session.post('https://cf.ddot.cc/api/redis',
                                        json=payload) as resp:
                    await resp.text()
            except Exception as e:
                cf.error(e)
            await asyncio.sleep(120)


async def start_cloudflared(port: int):
    await _start_bin('cloudflared',
                     *['tunnel', '--url', 'http://localhost:{}'.format(port)])


class App(object):

    @staticmethod
    def start(port: int = 80):
        """start both nsqlookupd and nsqd"""
        asyncio.run(startall(port))


def main():
    fire.Fire(App)
