#!/usr/bin/env python3
"""A function to generate random numbers"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """A function to generate"""

    list_generated = [number async for number in (async_generator())]
    return list_generated
