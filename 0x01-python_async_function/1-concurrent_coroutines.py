#!/usr/bin/env python3
"""
This is multiple coroutine with the async
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Executing Multiple Coroutine thesame time with async
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
