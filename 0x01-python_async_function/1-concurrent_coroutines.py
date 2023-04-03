#!/usr/bin/env python3
"""
Multiple
"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
     Executing Multiple Coroutine withthe async
     """
    delays = []
    for _ in range(n):
        delay = await wait_random(max_delay)
        delays.append(delay)
    delays = sorted(delays)
    return delays
