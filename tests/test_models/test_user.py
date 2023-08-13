#!/usr/bin/python3
"""Unittests for the user module"""

import models
import unittest
from datetime import datetime
from models.user import User


class TestUser(unittest.TestCase):
    """
    Unittest class for the User Module
    """

    def test_instance_creation(self):
        """Test creation of User instance"""
        self.assertIsInstance(User(), User)

    def test_user_instance_id(self):
        """Test user instance has id"""
        user = User()
        self.assertIn(user.id, user.__dict__["id"])

    def test_unique_user_instance_id(self):
        """Test user instances unique id"""
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)

    def test_user_instance_storage(self):
        """Test storage of user instance attributes"""
        self.assertIn(User(), models.storage.all().values())

    def test_user_email_type(self):
        """Test if user email is str"""
        self.assertIsInstance(User().email, str)

    def test_user_password_type(self):
        """Test if user password is str"""
        self.assertIsInstance(User().password, str)

    def test_user_firstname_type(self):
        """Test first name type is str"""
        self.assertIsInstance(User().first_name, str)

    def test_user_lastname_type(self):
        """Test user last name type"""
        self.assertIsInstance(User().last_name, str)

    def test_instace_created_at(self):
        """Test user instance creation timestamp"""
        self.assertEqual(datetime, type(User().created_at))

    def test_instance_updated_at(self):
        """Test user instance updation timestamp"""
        self.assertEqual(datetime, type(User().updated_at))

    def test_instance_args(self):
        """Test instance creation with args"""
        user = User(None)
        self.assertNotIn(None, user.__dict__.values())

    def test_save_user_instance(self):
        """Test saving user instance"""
        user = User()
        user.save()
        with open("file.json", "r") as file:
            self.assertIn(user.id, file.read())

    def test_dict_representation(self):
        """Test dictionary representation of instance"""
        self.assertEqual(type(User().to_dict()), dict)


if __name__ == "__main__":
    unittest.main()
