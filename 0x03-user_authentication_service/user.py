#!/usr/bin/env python3
"""Define User Model"""
from sqlalchemy import Column, Integer, String


class User():
    """ User Model"""
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    session_id = Column(String, nullable=False)
    reset_token = Column(String, nullable=True)
