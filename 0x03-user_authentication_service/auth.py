#!/usr/bin/env python3
"""Authentication Model"""
from bcrypt import hashpw, gensalt

salt = gensalt()


def _hash_password(password: str) -> bytes:
    """
    Encrypts a password
    """
    password = password.encode('utf-8')
    return hashpw(password, salt)
