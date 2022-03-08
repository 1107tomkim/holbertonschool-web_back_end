#!/usr/bin/env python3
"""Session auth"""
from api.v1.auth.auth import Auth
from flask import request
from models.user import User
from typing import TypeVar
import uuid


class SessionAuth(Auth):
    """Class object Session Auth
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Creates a ID for user id
        """
        if user_id is None or type(user_id) is not str:
            return (None)
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id.update({session_id: user_id})
        return (session_id)

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Returns use id based on session id
        """
        if session_id is None or type(session_id) is not str:
            return (None)
        return self.user_id_by_session_id.get(session_id)
