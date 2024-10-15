#!/usr/bin/env python3
"""Generate a list from an async comprehension"""
from typing import list
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> list[float]:
    """Collect async generated list and return it"""
    return [_ async for _ in async_generator()]
