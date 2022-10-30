#!/usr/bin/python3
"""Holds class State that inherits from BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    """State that inherits from BaseModel
     Attributes:
        name (str): user name
    """
    name = ""
