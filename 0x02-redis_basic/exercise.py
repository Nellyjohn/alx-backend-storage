#!/usr/bin/env python3
"""Module Docs"""
import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    def __init__(self):
        """Initializes a Redit client"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Takes a data argument and returns a string"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) ->
            Union[str, bytes, int, float, None]:
        """
        Take a key string argument and an optional Callable argument named fn
        """
        value = self._redis.get(key)
        if value is None:
            return None
        if fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> Optional[str]:
        """Function Docs"""
        return self.get(key, fn=lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """Function Docs"""
        return self.get(key, fn=int)
