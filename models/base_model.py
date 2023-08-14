#!/usr/bin/python3
"""
This module defines the BaseModel class.
"""

from datetime import datetime
import models
import uuid

DATE_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """
    Defines the BaseModel class.

    Attributes:
        id (str): The unique identifier for each instance.
        created_at (datetime): timestamp for when instance was created.
        updated_at (datetime): timestamp when the instance was last updated.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        if kwargs:
            if "__class__" in kwargs:
                del kwargs["__class__"]

            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    kwargs[key] = datetime.strptime(
                        value, DATE_FORMAT
                    )
            self.__dict__.update(kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """Updates the instance's updated_at attribute and saves
        the changes to storage.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Converts the instance into a dictionary representation.

        Returns:
            dict: contains the instance attributes and class name.
        """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict

    def __str__(self):
        """Returns a string representation of the instance.
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )
