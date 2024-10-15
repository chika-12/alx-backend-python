#!/usr/bin/env python3
"""A function to generate random numbers"""

import asyncio
import random


async def async_generator() -> float:
    """A function that loops 10 times"""

    for _ in range(10):
        await asyncio.sleep(1)
        delay = random.uniform(0, 10)
        yield delay
