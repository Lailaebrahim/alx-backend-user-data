#!/usr/bin/env python3
"""Module for Session Authentication Class
"""
from typing import List, TypeVar
from api.v1.auth.auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """SessionAuth Class

    This class represents the session-based authentication mechanism.
    """
    """SessionAuth Class"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Creates a session for the given user ID.

        Args:
            user_id (str): The ID of the user. Defaults to None.

        Returns:
            str: The session ID generated for the user.
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        Session_ID = str(uuid4())
        self.user_id_by_session_id[Session_ID] = user_id
        return Session_ID

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Retrieves the user ID associated with the given session ID.

        Args:
            session_id (str): The session ID to retrieve the user ID for.

        Returns:
            str: The user ID associated with the session ID, or
            None if the session ID is invalid.
        """
        if session_id is None or not isinstance(session_id, str) or\
                session_id not in self.user_id_by_session_id:
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """_summary_

        Args:
            request (_type_, optional): _description_. Defaults to None.
        """
        if request is None:
            return None
        cookie = self.session_cookie(request)
        if cookie is None:
            return None
        user_id = self.user_id_for_session_id(cookie)
        if user_id is None:
            return None
        from models.user import User
        user = User.get(user_id)
        if user is None:
            return None
        return user

    def destroy_session(self, request=None):
        """
        Destroys the session associated with the given request.
        Args:
            request (Request, optional): The request object.
            Defaults to None.
        Returns:
            bool: True if the session was successfully destroyed,
            False otherwise.
        """
        if request is None or self.session_cookie(request) is None:
            return False
        if self.user_id_for_session_id(self.session_cookie(request)) is None:
            return False
        session_id = self.session_cookie(request)
        if session_id is not None:
            del self.user_id_by_session_id[session_id]
            return True
        return False
