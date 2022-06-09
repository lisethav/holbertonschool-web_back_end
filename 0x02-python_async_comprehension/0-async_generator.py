#!/usr/bin/env python3
"""0. Async Generator"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """yield a random number between 0 and 10"""
    for i in range(10):
        random_number = random.uniform(0, 10)
        yield random_number
        await asyncio.sleep(1)
