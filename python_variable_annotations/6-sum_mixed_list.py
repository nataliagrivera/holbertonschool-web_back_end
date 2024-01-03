#!/usr/bin/env python3
from typing import Union, List
"""Basic annotations - mixed list"""


def sum_mixed_list(mxd_lst: List[Union(int, float)]) -> float:
    """Calculate the sum of a list of floats and integers"""
    return sum(mxd_lst)
