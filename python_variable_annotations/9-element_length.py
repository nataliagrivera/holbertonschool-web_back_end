#!/usr/bin/env python3
"""Let's duck type an iterable object"""


from typing import Iterable, List, Tuple


def element_length(lst: List[Iterable]) -> List[Tuple[Iterable, int]]:
    """function that return a list of tuples"""
    return [(i, len(i)) for i in lst]
