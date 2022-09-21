#!/usr/bin/env python3
""" 1. Let's execute multiple coroutines at the same time with async """

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """return the delay values Parameters"""
    spawn_list = []
    sorted_delays = []

    for i in range(n):
        spawn_list.append(wait_random(max_delay))

    for future in asyncio.as_completed(spawn_list):
        res = await future
        sorted_delays.append(res)

    return sorted_delays