#!/usr/bin/python3
"""City module"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    Defines the class City

    Attrubutes:
        state_id (str): unique id of the state
        name (str): name of the city
    """
    state_id = ""
    name = ""
