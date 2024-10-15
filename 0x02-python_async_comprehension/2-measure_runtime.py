#!/usr/bin/env pythons
"""Measure runtime and a return a total of it"""
import asyncio
import time
async_comphrehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Executes asyn_comprehension 4 times in parallel
        and measure_runtime should measure the total runtime and return it"""
        start_runtime = time.perf_counter()
        await asyncio.gather(async_comprehension(), async_comprehension(),                
                async_comprehension(), async_comprehension())
        return time.perf_counter() - start_time
