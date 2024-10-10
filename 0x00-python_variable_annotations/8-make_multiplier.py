#!/usr/bin/env python3
"""A function that return a function"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """A function that returns a function"""
    def mul(num: float) -> float:
        return num * multiplier
    return mul
