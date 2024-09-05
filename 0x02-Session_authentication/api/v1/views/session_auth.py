#!/usr/bin/env python3
""" Module of Authentication views
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """_summary_

    Args:
        request (_type_): _description_
    """
    email = request.form.get('email')
    if email is None or email == '' or not isinstance(email, str):
        return jsonify({"error": "email missing"}), 400
    password = request.form.get('password')
    if password is None or password == '' or not isinstance(password, str):
        return jsonify({"error": "password missing"}), 400
    from models.user import User
    users = User.search({"email": email})
    if users is None or users == []:
        return jsonify({"error": "no user found for this email"}), 404
    for user in users:
        if user.is_valid_password(password):
            from api.v1.app import auth
            session = auth.create_session(user.id)
            response = jsonify(user.to_json())
            from os import getenv
            response.set_cookie(getenv('SESSION_NAME'), session)
    
    
