#!/usr/bin/env python3
"""
Main file
"""

import logging
from db import DB
from user import User

# Disable logging
logging.disable(logging.CRITICAL)

my_db = DB()

user_1 = my_db.add_user("test@test.com", "SuperHashedPwd")
print(user_1.id)

user_2 = my_db.add_user("test1@test.com", "SuperHashedPwd1")
print(user_2.id)
