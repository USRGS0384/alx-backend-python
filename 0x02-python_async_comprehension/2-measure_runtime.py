#!/usr/bin/env python3
"""
An asynchronous function that measures the runtime
of running 4 instances of the asyn_comprehension function from the
'1-async_comprehension' module
"""
import asyncio
import time
from importlib import import_module as using

async_comprehension = using('1-async_comprehension').asyc_comprehension


async def measure_runtime() -> float:
    """
    Asynchronous function that meaures and returns the runtime of
    running 4 instances of the async_comprehension function.

    Returns:
    float: the runtime of the async_comprehension function in seconds
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time
