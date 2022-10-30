#!/usr/bin/python3
"""Holds class City that inherits from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """City that inherits from BaseModel
     Attributes:
        name (str): user name
        state_id (str): state id
    """
    state_id = ""
    name = ""
