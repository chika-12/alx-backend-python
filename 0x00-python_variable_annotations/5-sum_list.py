#!/usr/bin/env python3
"""A function to add up the list"""


def sum_list(input_list: float) -> float:
    """A function that returns the sum of a list of floats"""
    result = 0.0
    for num in input_list:
        result += num
    return result
