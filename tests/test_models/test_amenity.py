#!/usr/bin/python3
"""Unittest for the Amenity module"""

import models
import unittest
from datetime import datetime
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Defines the test cases for the Amenity module"""

    def test_instance(self):
        """Test instance creation of the Amenity module"""
        self.assertEqual(Amenity, type(Amenity()))

    def test_instance_storage(self):
        """Test storage of new instance"""
        self.assertIn(Amenity(), models.storage.all().values())

    def test_instance_id(self):
        """Test instance id"""
        self.assertEqual(type(Amenity().id), str)

    def test_instance_created_at(self):
        """Test creation timestamp"""
        self.assertEqual(type(Amenity().created_at), datetime)

    def test_instance_updated_at(self):
        """Test updation timestamp"""
        self.assertEqual(type(Amenity().updated_at), datetime)

    def test_instance_with_id(self):
        """Test instance creation with id"""
        a = Amenity(id="12345")
        self.assertEqual(a.id, "12345")

    def test_instance_with_none_timestamps(self):
        """Test object init with None timestamp"""
        with self.assertRaises(TypeError):
            a = Amenity(created_at=None, updated_at=None)

    def test_to_dict(self):
        """Test to_dict method"""
        self.assertEqual(type(Amenity().to_dict()), dict)

    def test_correct_id_key(self):
        """Test dictionary has correct key"""
        a = Amenity()
        self.assertIn("id", a.to_dict())

    def test_correct_timestamp_key(self):
        """Test dictionary has correct timestamp key"""
        a = Amenity()
        self.assertIn("created_at", a.to_dict())
        self.assertIn("updated_at", a.to_dict())
