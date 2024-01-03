#!/usr/bin/env python3
from typing import List
"""Module that calculates the sum of a list of floats"""""


def sum_list(input_list: list) -> float:
    """Calculate the sum of a list of floats"""
    if all(isinstance(item, float) for item in input_list):
        return sum(input_list)
    else:
        raise TypeError("Input list should contain only floats")
