#!/usr/bin/python3
"""This module creates a City class"""

from models.base_model import BaseModel


class City(BaseModel):
    """Class for managing city objects"""

    state_id = ""
    name = ""
