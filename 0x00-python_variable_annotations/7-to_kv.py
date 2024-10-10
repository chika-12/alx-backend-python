#!/usr/bin/env python3
"""A function that returns a turple"""

from typing import Tuple


def to_kv(k: str, v: float) -> Tuple[str, float]:
    """A function for returning a tuple"""
    return (k, v**2)
