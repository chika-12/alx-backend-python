#!/usr/bin/env python3
"""A python function to help return the runtime of
    other functions execution
"""


import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """A function"""
    start = time.time()
    for _ in range(4):
        await asyncio.gather(async_comprehension())
    end = time.time()
    return end - start
