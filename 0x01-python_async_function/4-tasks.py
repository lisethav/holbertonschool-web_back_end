#!/usr/bin/env python3
""" 4. Tasks """

from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """ Return the delay values """
    spawn_list = []
    sorted_delays = []

    for i in range(n):
        spawn_list.append(task_wait_random(max_delay))

    for future in asyncio.as_completed(spawn_list):
        res = await future
        sorted_delays.append(res)

    return sorted_delays
