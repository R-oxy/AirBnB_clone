#!/usr/bin/python3
""" Place module """
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class that inherits from BaseModel.
    Public class attributes:
        city_id: string - The UUID of the City the Place is located in
        user_id: string - The UUID of the User of the Place
        name: string - The Place name
        description: string - The Place description
        number_rooms: integer - The number of rooms in the Place
        number_bathrooms: integer - The number of bathrooms in the Place
        max_guest: integer - maximum number of guests for the place
        price_by_night: integer - The price per night
        latitude: float - The latitude of the place
        longitude: float - The longitude of the Place
        amenity_ids: list of string - A list that contains all the Amenities in the Place
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
