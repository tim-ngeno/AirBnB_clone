#!/usr/bin/python3
"""
Review Module
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class inherits from BaseModel

    Attributes:
        place_id (str): Place ID.
        user_id (str): User ID.
        text (str): Review text.
    """
    place_id = ""
    user_id = ""
    text = ""
