#!/usr/bin/python3
"""The User model"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Defines the User module

    Attributes:
        email (str): user email address
        password (str): user password
        first_name (str): User's first name
        last_name (str): User's last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
