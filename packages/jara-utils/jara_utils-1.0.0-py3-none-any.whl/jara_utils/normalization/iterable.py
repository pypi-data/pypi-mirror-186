from typing import Iterable, Generator, AsyncIterable, AsyncGenerator

import itertools


def grouper(n: int, iterable: Iterable) -> Generator:
    it = iter(iterable)
    while True:
        chunk = tuple(itertools.islice(it, n))
        if not chunk:
            return
        yield chunk


async def aenumerate(async_iterable: AsyncIterable, start: int = 0, /) -> AsyncGenerator:
    i = start
    async for element in async_iterable:
        yield i, element
        i += 1


async def async_grouper(n: int, async_iterable: AsyncIterable) -> AsyncGenerator:
    chunk = []
    async for i, element in aenumerate(async_iterable, 1):
        chunk.append(element)
        if i % n == 0:
            yield tuple(chunk)
            chunk = []
    if chunk:
        yield chunk
