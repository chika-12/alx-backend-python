#!/usr/bin/env python3
"""A function spawning await"""

import asyncio
import random
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """A function"""

    delay_list = []

    for _ in range(n):
        delay = await wait_random(max_delay)
        delay_list.append(delay)
    return delay_list
