#!/usr/bin/env python3
""" Lines code """


from functools import wraps
import redis
from typing import Union, Optional, Callable
from uuid import uuid4


def count_calls(method: Callable) -> Callable:
    """ Lines code """

    llave = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Lines code """
        self._redis.incr(llave)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """ Lines code """

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Lines code """
        ent = str(args)
        self._redis.rpush(method.__qualname__ + ":inputs", ent)
        salida = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + ":outputs", salida)
        return salida
    return wrapper


def replay(fn: Callable):
    """ Lines code """
    rea = redis.Redis()
    f_n = fn.__qualname__
    n_c = rea.get(f_n)
    try:
        n_c = n_c.decode('utf-8')
    except Exception:
        n_c = 0
    print(f'{f_n} was called {n_c} times:')

    ins = rea.lrange(f_n + ":inputs", 0, -1)
    outs = rea.lrange(f_n + ":outputs", 0, -1)

    for int, output in zip(ins, outs):
        try:
            int = int.decode('utf-8')
        except Exception:
            int = ""
        try:
            output = output.decode('utf-8')
        except Exception:
            output = ""
        print(f'{f_n}(*{int}) -> {output}')


class Cache:
    """ Lines code """

    def __init__(self) -> None:
        """ constructor codes """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Lines code """
        random_key = str(uuid4())
        self._redis.set(random_key, data)
        return random_key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """ Lines code """
        val = self._redis.get(key)
        return fn(val) if fn else val

    def get_str(self, key: str) -> str:
        """ Lines code """
        return self._redis.get(key).decode("utf-8")

    def get_int(self, key: str) -> int:
        """ Lines code """
        val = self._redis.get(key)
        try:
            val = int(val.decode("utf-8"))
        except ValueError:
            val = 0
        return val