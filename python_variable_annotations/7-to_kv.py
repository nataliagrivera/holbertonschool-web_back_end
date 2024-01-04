#!/usr/bin/env python3
"""Complex types - string and int/float to tuple"""


from typing import Union, Tuple


def to_kv(k: str, v: Tuple[Union[int, float]]) -> Tuple[str, float]:
    """Returns a tuple"""
    return (k, v * v)
