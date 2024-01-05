#!/usr/bin/env python3
"""Basic async syntax"""


import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random delay between 0 and max_delay"""
    random_delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
