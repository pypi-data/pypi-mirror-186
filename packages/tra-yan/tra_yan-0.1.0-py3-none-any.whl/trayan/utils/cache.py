from asyncio import iscoroutinefunction, ensure_future, Future
from time import time
from typing import Optional, Callable, Union, Awaitable, Any


class cached_property:
    def __init__(self, ttl: Optional[int] = None):
        if callable(ttl):
            func = ttl
            ttl = None
        else:
            func = None
        self.ttl = ttl
        self._prepare_func(func)

    def __call__(self, func, doc=None):
        self._prepare_func(func, doc)
        return self

    def __get__(self, obj, cls):
        now = time()
        if cache := obj.__dict__.get(self.__name__):
            cache_value, last_updated = cache
            if not (self.ttl and self.ttl < now - last_updated):
                return cache_value
        cache = ensure_future(self.func(obj)) if iscoroutinefunction(self.func) else self.func(obj)
        self._update_cache(obj, cache, now)
        return cache

    def __set__(self, obj, value):
        now = time()
        if iscoroutinefunction(self.func):
            future = Future()
            future.set_result(value)
            value = future
        self._update_cache(obj, value, now)

    def __delete__(self, obj):
        obj.__dict__.pop(self.__name__, None)

    def _prepare_func(self, func: Union[Callable, Awaitable], doc: Optional[str] = None) -> None:
        self.func = func
        if func:
            self.__doc__ = doc or getattr(func, '__doc__')
            self.__name__ = func.__name__
            self.__module__ = func.__module__

    def _update_cache(self, obj: Callable, cache: Any, now: float) -> None:
        obj.__dict__[self.__name__] = (cache, now)
