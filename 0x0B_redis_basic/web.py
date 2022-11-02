#!/usr/bin/env python3
""" lines code """

from functools import wraps
import redis
from requests import get
from typing import Callable

ro = redis.Redis()


def count_requests(method: Callable) -> Callable:
    """ lines code """

    @wraps(method)
    def wrapper(url):
        """ lines code """
        ro.incr(f"count:{url}")
        cached_html = ro.get(f"cached:{url}")
        if cached_html:
            return cached_html.decode('utf-8')
        html = method(url)
        ro.setex(f"cached:{url}", 10, html)
        return html
    return wrapper


@count_requests
def get_page(url: str) -> str:
    """ lines code """
    res = get(url)
    return res.text
