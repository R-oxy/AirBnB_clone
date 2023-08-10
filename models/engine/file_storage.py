#!/usr/bin/python3
"""
Hbnb clone FileStorage class definition.
"""
import json
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review



class FileStorage:
    """
    Serializes and deserializes instances to/from JSON files.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file.
        """
        serialized = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(serialized, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the file exists).
        """
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                for key, value in data.items():
                    module_name, obj_id = key.split(".")
                    cls = __import__(module_name, fromlist=[module_name])
                    if module_name == "base_model":
                        instance = BaseModel(**value)
                    elif module_name == "state":
                        instance = State(**value)
                    elif module_name == "city":
                        instance = City(**value)
                    elif module_name == "amenity":
                        instance = Amenity(**value)
                    elif module_name == "place":
                        instance = Place(**value)
                    elif module_name == "review":
                        instance = Review(**value)
                    else:
                        continue
                    FileStorage.__objects[key] = instance
        except FileNotFoundError:
            pass
