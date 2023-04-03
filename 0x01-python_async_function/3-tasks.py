#!/usr/bin/env python3
"""
sync func
"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Now a function task_wait_random takes an interger max_delay to return asynio.Task
    """
    Task = asyncio.create_task(wait_random(max_delay))

    return Task
