#!/usr/bin/env python3
""" module for async routine """

from typing import List
import asyncio

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ spawn task_wait_random task n times with the specified max_delay """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
