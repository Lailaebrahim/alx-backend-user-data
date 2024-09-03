#!/usr/bin/env python3
"""Module for auth views
"""
from flask import request
from typing import List, TypeVar


class Auth():
    """Auth Class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Args:
            path (str):
            excluded_paths (List[str]):

        Returns:
            bool: False
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Args:
            request ([type], optional):. Defaults to None.

        Returns:
            str:
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Args:
            request ([type], optional):. Defaults to None.

        Returns:
            TypeVar('User'):
        """
        return None
