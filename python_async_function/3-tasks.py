#!/usr/bin/env python3
"""Tasks"""
from typing import List
import asyncio
import random


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Return a asyncio.Task"""
    return asyncio.create_task(wait_random(max_delay))
