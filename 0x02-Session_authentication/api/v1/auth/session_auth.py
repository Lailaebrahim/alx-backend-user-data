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

        Args:
            user_id (str, optional): _description_. Defaults to None.

        Returns:
            str: _description_
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        Session_ID = uuid4()
        self.user_id_by_session_id[Session_ID] = user_id
        return Session_ID

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """_summary_
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)
