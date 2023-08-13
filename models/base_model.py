#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    BaseModel class that defines common attributes/methods for other classes.
    Public instance attributes:
        id: string - assign with an uuid when an instance is created
        created_at: datetime - assign with the current datetime when an instance is created
        updated_at: datetime - update every time you change your object
    Public instance methods:
        save(self): updates the public instance attribute updated_at with the current datetime
        to_dict(self): returns a dictionary containing all keys/values of __dict__ of the instance
    """
    def __init__(self, *args, **kwargs):
        """ Initializes BaseModel instance """
        from models import storage
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """ Updates updated_at with the current datetime """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ Returns dictionary representation of the instance """
        new_dict = dict(self.__dict__)
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
