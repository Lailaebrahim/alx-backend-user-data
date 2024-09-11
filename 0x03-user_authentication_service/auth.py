#!/usr/bin/env python3
"""Authentication Model"""
from bcrypt import hashpw, gensalt, checkpw
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound

salt = gensalt()


def _hash_password(password: str) -> bytes:
    """
    Encrypts a password
    """
    password = password.encode('utf-8')
    return hashpw(password, salt)


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Register A new user to db

        Args:
            email (str): user email shall be unique
            password (str): user unhashed password

        Returns:
            User: newly created password
        """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hased_password = _hash_password(password)
            return self._db.add_user(email, hased_password)
    
    def valid_login(self, email: str, password: str) -> bool:
        """_summary_

        Args:
            email (str): _description_
            password (str): _description_
        """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                return checkpw(password.encode('utf-8'), user.hashed_password)
        except Exception:
            return False
