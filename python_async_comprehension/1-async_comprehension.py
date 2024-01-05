#!/usr/bin/env python3
"""Async comprehension"""


from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Return a list of all the random numbers"""
    return [number async for number in async_generator()]
