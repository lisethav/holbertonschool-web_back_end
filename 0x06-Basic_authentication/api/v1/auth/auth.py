#!/usr/bin/env python3
"""
API Authentication
"""


from flask import request
from typing import List, TypeVar
import fnmatch


class Auth():
    """Authentication class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Nothing so far
        """
        if path is None:
            return True
        if excluded_paths is None:
            return True
        my_list = [x[:-1] for x in excluded_paths if x[-1] == '/']
        if path in excluded_paths or path in my_list:
            return False
        for ex in excluded_paths:
            if fnmatch.fnmatch(path, ex):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """Nothing so far
        """
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        return request.headers['authorization']

    def current_user(self, request=None) -> TypeVar('user'):
        """Nothign so far
        """
        return None