#!/usr/bin/python3
"""Importing class BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """class attributes"""

    place_id = ""
    user_id = ""
    text = ""
