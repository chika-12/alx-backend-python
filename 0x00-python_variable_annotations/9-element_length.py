#!/usr/bin/env python3
"""A function"""

from typing import List, Tuple, Iterable


def element_length(lst: List[Iterable]) -> List[Tuple[Iterable, int]]:
    """A function"""
    return [(i, len(i)) for i in lst]
