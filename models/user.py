#!/usr/bin/python3
""" Defines a class User """
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class that inherits from BaseModel.
    Public class attributes:
        email: string - The User email
        password: string - The User password
        first_name: string - The first name of the User
        last_name: string - The last name of the User
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
