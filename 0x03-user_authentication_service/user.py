#!/usr/bin/env python3
"""Define User Model"""
from sqlalchemy import Column, Integer, VARCHAR


class User():
    """ User Model"""
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(VARCHAR(250), nullable=False)
    hashed_password = Column(VARCHAR(250), nullable=False)
    session_id = Column(VARCHAR(250), nullable=False)
    reset_token = Column(VARCHAR(250), nullable=True)
