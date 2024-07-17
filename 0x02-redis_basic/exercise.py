#!/usr/bin/env python3
"""
Wrinting strings to redis
"""
import redis
from uuid import uuid4
from typing import Union, Optional, Callable


class Cache:
    """
    connect to redis
    """
    def __init__(self):
        """
        create redis instatce
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        store data
        """
        rkey = str(uuid4())
        self._redis.set(rkey, data)
        return rkey

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        '''convert the data back to the desired format'''
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        '''parametrize Cache.get with correct conversion function'''
        value = self._redis.get(key)
        return value.decode("utf-8")

    def get_int(self, key: str) -> int:
        '''parametrize Cache.get with correct conversion function'''
        value = self._redis.get(key)
        try:
            value = int(value.decode("utf-8"))
        except Exception:
            value = 0
        return value
