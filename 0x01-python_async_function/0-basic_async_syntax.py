!/usr/bin/env python3
"""
Assync Execution
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    asynchronous coroutine that will takes in an
    integer argument
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
