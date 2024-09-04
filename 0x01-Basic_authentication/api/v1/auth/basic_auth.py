#!/usr/bin/env python3
"""Module for Basic auth Class
"""
import base64
from api.v1.auth.auth import Auth
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """Basic Auth class
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str,
                                            ) -> str:
        """returns the Base64 part of the Authorization
        header for a Basic Authentication
        """
        if authorization_header is None or \
                not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str,
                                           ) -> str:
        """
        Method that returns the decoded value
        of a Base64 string base64_authorization_header
        Args:
            base64_authorization_header (str):
            the encoded value of a Base64 string

        Returns:
            str: the decoded value of base64_authorization_header
        """
        if base64_authorization_header is None \
                or not isinstance(base64_authorization_header, str):
            return None
        try:
            return base64.b64decode(base64_authorization_header)\
                .decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str,
                                 ) -> (str, str):
        """_summary_

        Args:
            self (_type_): _description_
            str (_type_): _description_
        """
        if decoded_base64_authorization_header is None or \
                not isinstance(decoded_base64_authorization_header, str)\
                or ':' not in decoded_base64_authorization_header:
            return None, None
        return tuple(decoded_base64_authorization_header.split(':', 1))

    def user_object_from_credentials(self,
                                     user_email: str,
                                     user_pwd: str,
                                     ) -> User:
        """
        Retrieve a User object based on the provided email and password.
            user_email (str): The email of the user.
            user_pwd (str): The password of the user.
        Returns:
            User: The User object if the email and password match,
            otherwise None.
        """
        if user_email is None or \
                not isinstance(user_email, str) or \
                user_pwd is None or not isinstance(user_pwd, str):
            return None
        try:
            users = User.search({'email': user_email})
        except Exception:
            return None
        if users == []:
            return None
        for user in users:
            if user.is_valid_password(user_pwd):
                return user
        return None


    def current_user(self, request=None) -> User:
        """_summary_

        Args:
            request (_type_, optional): _description_. Defaults to None.

        Returns:
            User: _description_
        """
        try:
            auth_header = self.authorization_header(request)
            base64_auth_header = self.extract_base64_authorization_header(auth_header)
            auth_header = self.decode_base64_authorization_header(
                base64_auth_header)
            user_credentials= self.extract_user_credentials(auth_header)
            return self.user_object_from_credentials(user_credentials.get(0),
                                                     user_credentials.get(1))
        except Exception:
            return None
