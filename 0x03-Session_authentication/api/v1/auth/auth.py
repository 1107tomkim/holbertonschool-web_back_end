#!/usr/bin/env python3
"""API Authentication"""
from flask import request
from typing import List, TypeVar


class Auth():
    """Class Auth"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        def method require auth that returns False - path
        and exculuded_paths
        """
        if path is None or excluded_paths is None:
            return True
        if path in excluded_paths or f"{path}/" in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        def method auth header that returns None - request
        """
        if request is None or request.headers.get('Authorization') is None:
            return (None)
        return (request.headers.get('Authorization'))

    def current_user(self, request=None) -> TypeVar('User'):
        """
        def method current user that returns None - request
        """
        return (None)

    def session_cookie(self, request=None):
        """
        def method session cookie returns val from request
        """
        if request is None:
            return None
        _my_session_id = getenv('SESSION_NAME')
        return request.cookies.get(_my_session_id)
