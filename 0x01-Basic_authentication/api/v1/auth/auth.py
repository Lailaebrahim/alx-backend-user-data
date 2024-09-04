#!/usr/bin/env python3
"""Module for auth views
"""
from flask import request
from typing import List, TypeVar


class Auth():
    """Auth Class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Method to check if the requested path require authentication
        Args:
            path (str):
            excluded_paths (List[str]):

        Returns:
            bool: False
        """
        if path is None or excluded_paths is None or excluded_paths == []:
            return True
        if path[-1] != '/':
            path += '/'
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        Get The value of the AUthorization header of the request
        Args:
            request ([type], optional):. Defaults to None.

        Returns:
            str:
        """
        if request is None or request.get('Authorization'):
            return None
        return request.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Args:
            request ([type], optional):. Defaults to None.

        Returns:
            TypeVar('User'):
        """
        return None
