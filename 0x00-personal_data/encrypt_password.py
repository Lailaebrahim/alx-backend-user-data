#!/usr/bin/env python3
"""Password Hashing"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Takes in a password string arguments and
    returns a salted, hashed password"""
    return bcrypt.hashpw(password.encode('utf-8'),
                         bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Check hashed passwords"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
