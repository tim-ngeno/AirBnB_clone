#!/usr/bin/python3
"""
Unittest for file storage module
"""
import models
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.engine.file_storage import FileStorage
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class TestFileStorage(unittest.TestCase):
    """Defines test cases for the FileStorage module"""

    def test_instance(self):
        """Test creation of a FileStorage object"""
        self.assertEqual(FileStorage, type(FileStorage()))

    def test_instance_attributes_filepath(self):
        """Test instance attribute filepath"""
        self.assertEqual(str, type(
            FileStorage._FileStorage__file_path
        ))

    def test_instance_attributes_objects(self):
        """Test instance attribute objects"""
        self.assertEqual(dict, type(
            FileStorage._FileStorage__objects
        ))

    def test_storage(self):
        """Test storage type"""
        self.assertEqual(FileStorage, type(models.storage))

    def test_storage_objects(self):
        """Test storage of all objects"""
        self.assertEqual(dict, type(models.storage.all()))

    def test_storage_new_base_model(self):
        """Test storage of new base_model instance"""
        b = BaseModel()
        models.storage.new(b)
        self.assertIn(
            "BaseModel." + b.id, models.storage.all().keys()
        )

    def test_storage_new_user(self):
        """Test storage of new user instance"""
        u = User()
        models.storage.new(u)
        self.assertIn("User." + u.id, models.storage.all().keys())

    def test_storage_new_state(self):
        """Test storage of new state"""
        state = State()
        models.storage.new(state)
        self.assertIn(
            "State." + state.id, models.storage.all().keys()
        )

    def test_storage_new_place(self):
        """Test storage of new place"""
        place = Place()
        models.storage.new(place)
        self.assertIn(
            "Place." + place.id, models.storage.all().keys()
        )

    def test_storage_new_city(self):
        """Test storage of new city"""
        city = City()
        models.storage.new(city)
        self.assertIn(
            "City." + city.id, models.storage.all().keys()
        )

    def test_storage_new_amenity(self):
        """Test storage of new amenity"""
        amenity = Amenity()
        models.storage.new(amenity)
        self.assertIn(
            "Amenity." + amenity.id, models.storage.all().keys()
        )

    def test_storage_new_review(self):
        """Test storage of new review"""
        review = Review()
        models.storage.new(review)
        self.assertIn(
            "Review." + review.id, models.storage.all().keys()
        )


if __name__ == "__main__":
    unittest.main()
