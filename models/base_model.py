from datetime import datetime
import uuid

class BaseModel:
    """Defines attributes and methods for all other classes"""
    
    def __init__(self, *args, **kwargs):
        """Initializes class BaseModel"""
        if kwargs is not None:
            dictionary = self.__dict__.copy()
            if 'created_at' in dictionary:
                dictionary['created_at'] = datetime.now()
            if 'updated_at' in dictionary:
                dictionary['updated_at'] = datetime.now()
        else:
            for key in kwargs:
                self.__dict__[key] = kwargs[key]

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns key/value pairs of __dict__"""
        dictionary = self.__dict__.copy()
        dictionary ['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        dictionary ['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        dictionary ['__class__'] = self.__class__.__name__
        return dictionary
