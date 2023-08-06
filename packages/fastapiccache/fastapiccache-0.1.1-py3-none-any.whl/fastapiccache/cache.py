import os
import time
import asyncio
import tempfile
import functools
from typing import Optional, Callable, Dict, Any


__all__ = ["FastAPICache", "fastapicache", "INMEMORY_CACHE"]

INMEMORY_CACHE = 0x1


class _CacheItemBase:

    __slots__ = ["func", "revalidate", "_start_record"]

    def __init__(self, func: Callable, revalidate: int) -> None:
        self.func = func
        self.revalidate = revalidate
        self._start_record = time.time()

    def results(self, *args, **kwargs) -> None:
        raise NotImplementedError()

    def async_results(self, *args, **kwargs) -> None:
        raise NotImplementedError()

    def expired(self) -> bool:
        """return wether the cache is expired"""
        return (
            self.revalidate != 0
            and int(time.time() - self._start_record) >= self.revalidate
        )


class _CacheInMemory(_CacheItemBase):
    """
    cache in memory simply checks for experation, if expired, call the function with
    the given args and kwargs, store the results in a variable, and return the
    value of the variable until experation
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._results = None

    def results(self, *args, **kwargs) -> None:
        if not self._results or self.expired():
            self._results = self.func(*args, **kwargs)
            self._start_record = time.time()
        return self._results

    async def async_results(self, *args, **kwargs) -> None:
        if not self._results or self.expired():
            self._results = await self.func(*args, **kwargs)
            self._start_record = time.time()
        return self._results


_cache_methods = {
    INMEMORY_CACHE: _CacheInMemory
}


class FastAPICache:

    __slots__ = ["_hash_func"]

    def __init__(self, *, hash_func: Callable = hash) -> None:
        self._hash_func = hash_func

    def cache( self, func: Optional[Callable] = None, /, *, method: int = INMEMORY_CACHE, revalidate: int = 60, **kwargs) -> Callable:
        if func is not None:
            return self._cache(func)
        return functools.partial(
            self._cache, method=method, revalidate=revalidate, **kwargs
        )

    def _cache(self, func: Callable, /, *, method: int = INMEMORY_CACHE, revalidate: int = 60, **kwargs) -> Callable:
        if method not in _cache_methods:
            raise ValueError(f"unknown cache method {method} for {func.__name__}")
        cache_item = _cache_methods[method](func, revalidate, **kwargs)

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return cache_item.results(*args, **kwargs)

        @functools.wraps(func)
        async def async_wrapper(*args, **kwargs):
            return await cache_item.async_results(*args, **kwargs)

        if asyncio.iscoroutinefunction(func):
            return async_wrapper
        return wrapper


def fastapicache(*args, **kwargs):
    return FastAPICache().cache(*args, **kwargs)
