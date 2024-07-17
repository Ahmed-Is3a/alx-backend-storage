#!/usr/bin/env python3
"""
Wrinting strings to redis
"""
import redis
from uuid import uuid4
from typing import Union


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
