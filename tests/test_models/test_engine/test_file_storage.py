#!/usr/bin/python3
""" Unit tests for FileStorage class. """
import unittest
import os
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    Test cases for FileStorage class methods.
    """

    def setUp(self):
        self.file_path = FileStorage._FileStorage__file_path
        self.objects = FileStorage._FileStorage__objects
        self.base = BaseModel()
        self.state = State()
        self.city = City()
        self.amenity = Amenity()
        self.place = Place()
        self.review = Review()
        self.classes = {
            "BaseModel": BaseModel,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }

    def tearDown(self):
        try:
            os.remove(self.file_path)
        except FileNotFoundError:
            pass

    def test_file_path_exists(self):
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))

    def test_objects_exists(self):
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))

    def test_all_method(self):
        self.assertEqual(storage.all(), FileStorage._FileStorage__objects)

    def test_new_method(self):
        key = f"{self.base.__class__.__name__}.{self.base.id}"
        self.assertNotIn(key, self.objects)
        storage.new(self.base)
        self.assertIn(key, self.objects)

    def test_save_method(self):
        self.base.save()
        self.assertTrue(os.path.exists(self.file_path))
        with open(self.file_path, "r") as file:
            data = json.load(file)
            self.assertTrue(data)

    def test_reload_method(self):
        key = f"{self.base.__class__.__name__}.{self.base.id}"
        self.objects[key] = self.base
        self.base.save()
        self.objects.clear()
        self.assertFalse(self.objects)
        storage.reload()
        self.assertEqual(self.objects[key], self.base)

if __name__ == "__main__":
    unittest.main()
