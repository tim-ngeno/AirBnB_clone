#!/usr/bin/python3
"""
Unittest for model `city`
"""
import models
import unittest
from datetime import datetime
from models.city import City


class TestCity(unittest.TestCase):
    """Defines the unittests for module City"""

    def test_instance(self):
        """Test instance creation"""
        self.assertEqual(City, type(City()))

    def test_instance_with_state_id(self):
        """Test instance with id kwargs"""
        city = City(state_id="12345")
        self.assertEqual(city.state_id, "12345")

    def test_instance_with_name(self):
        """Test instance with name kwargs"""
        city = City(name="City")
        self.assertEqual(city.name, "City")

    def test_instance_attrs_id(self):
        """Test type of instance id is str"""
        self.assertEqual(type(City().id), str)

    def test_instance_attrs_created_at(self):
        """Test type of instance creation timestamp"""
        self.assertEqual(type(City().created_at), datetime)

    def test_instance_attrs_updated_at(self):
        """Test type of instance updation timestamp"""
        self.assertEqual(type(City().updated_at), datetime)

    def test_instance_stored(self):
        """Test instance is stored"""
        self.assertIn(City(), models.storage.all().values())

    def test_unique_instance_ids(self):
        """Test different instances have unique id"""
        c1 = City()
        c2 = City()
        self.assertNotEqual(c1.id, c2.id)


if __name__ == "__main__":
    unittest.main()
