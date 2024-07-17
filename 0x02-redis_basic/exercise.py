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

    def get(self, key: str, fn: Optional[Callable] = None) -> any:
        """
        get the value from redis
        key: string
        """
        value = self._redis.get(key)
        if fn:
            return fu(value)
        return value

    def get_str(self, key: str) -> str:
        """ get string """
        return self.get(key, fn=lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """ get integer """
        return self.get(key, fn=int)
