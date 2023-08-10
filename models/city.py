#!/usr/bin/python3
""" City module """
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class that inherits from BaseModel.
    Public class attributes:
        state_id: string - The UUID of the State the City belongs to
        name: string - name of the City
    """
    state_id = ""
    name = ""
