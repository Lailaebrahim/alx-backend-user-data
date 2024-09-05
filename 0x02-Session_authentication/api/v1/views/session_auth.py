#!/usr/bin/env python3
""" Module of Authentication views
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """
    Summary:
        This view handles the login functionality using session authentication.
        request (object): The request object containing the form data.
    Returns:
        - If the email or password is missing or not a string,
            it returns a JSON response
            with an error message and a status code of 400.
        - If no user is found for the given email, it returns a JSON response
            with an error message and a status code of 404.
        - If the password is valid, it creates a session for the user,
            sets a session cookie,
            and returns a JSON response with the user's data.
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
            return response
    return jsonify({"error": "wrong password"}), 401


@app_views.route('auth_session/logout', methods=['DELETE'], strict_slashes=False)
def logout():
    """
    Logout the user from the session.
    Returns:
        A JSON response with an empty dictionary and a status code of 200.
    Raises:
        404: If the session cannot be destroyed.
    """
    from api.v1.app import auth
    if auth.destroy_session(request) is False:
        abort(404)
    return jsonify({}), 200
