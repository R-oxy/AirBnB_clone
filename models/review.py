#!/usr/bin/python3
""" Review module """
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class that inherits from BaseModel.
    Public class attributes:
        place_id: string - The UUID of the Place the Review belongs to
        user_id: string - The UUID of the User that made the review
        text: string - message the user wrote about the place
    """
    place_id = ""
    user_id = ""
    text = ""
