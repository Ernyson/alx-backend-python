#!/usr/bin/env python3
"""
A sync func
"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    A fuction that takes an interger and return a asyncio
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
