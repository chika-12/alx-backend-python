#!/usr/bin/env python3
"""A function to generate random numbers"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """A function that loops 10 times"""

    for _ in range(10):
        await asyncio.sleep(1)
        delay = random.random() * 10
        yield delay
