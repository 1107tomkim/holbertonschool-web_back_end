#!/usr/bin/env python3
""" File to hold exercises to get more familiar with Redis """
from functools import wraps
from typing import Callable, Union
from uuid import uuid4
import redis


def count_calls(method: Callable) -> Callable:
    """Counts how many times methods of Cache is called"""

    @wraps(method)
    def wrapper(self, *args) -> Union[int, str]:
        """Increments counter on each call"""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args)
    return (wrapper)


def call_history(method: Callable) -> Callable:
    """Store history of inputs and outputs"""
    @wraps(method)
    def wrapper(self, *args) -> Union[int, str]:
        """Appends inputs and output to redis"""
        key = method.__qualname__
        self._redis.rpush(f"{key}:inputs", str(args))
        output = method(self, *args)
        self._redis.rpush(f"{key}:outputs", output)
        return (output)
    return (wrapper)


def replay(method: Callable) -> None:
    """Shows the history and how many times a method was called"""
    local_redis = redis.Redis()
    qn = method.__qualname__
    inputs = local_redis.lrange(f"{qn}:inputs", 0, -1)
    outputs = local_redis.lrange(f"{qn}:outputs", 0, -1)
    print(f"{qn} was called {len(inputs)} times:")
    for i, o in zip(inputs, outputs):
        print(f"{qn}(*{(i).decode('utf-8')}) -> {(o).decode('utf-8')}")


class Cache():
    """Class object Cache"""

    def __init__(self):
        """Initializes redis"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores data"""
        key = str(uuid4())
        self._redis.set(key, data)
        return (key)

    def get(self, key: str, fn: Callable = None) -> Union[str, int]:
        """Gets the format that is being requested"""
        if fn:
            return fn(self._redis.get(key))
        return self._redis.get(key)

    def get_str(self, key: str) -> str:
        """Returns String"""
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """Returns Int"""
        return self.get(key, int)
