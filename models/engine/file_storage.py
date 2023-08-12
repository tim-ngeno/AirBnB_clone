#!/usr/bin/python3
"""FileStorage module"""

import json
import os
from datetime import datetime
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.user import User

DATE_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"


class FileStorage:
    """
    Defines a class FileStorage that serializes/deserializes instances to/from JSON.

    Attributes:
        __file_path (str): Path to the JSON file.
        __objects (dict): Dictionary to store objects by <class name>.id.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Adds a new obj to the __objects dictionary with key <obj class name>.id.

        Args:
            obj: The object instance to be added.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file __file_path.
        """
        obj_dict = {key: value.to_dict()
                    for key, value in self.__objects.items()}
        with open(self.__file_path, "w") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        if the JSON file doesn't exist.
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as file:
                obj = json.load(file)
                for key, value in obj.items():
                    class_name = value["__class__"]
                    del value["__class__"]
                    # value['created_at'] = datetime.strptime(
                    #     value['created_at'], DATE_FORMAT)
                    # value['updated_at'] = datetime.strptime(
                    #     value['updated_at'], DATE_FORMAT)
                    data = eval(class_name + "(**value)")
                    self.__objects[key] = data
