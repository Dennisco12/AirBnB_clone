#!/usr/bin/python3
"""The Basemodel class that all other classes inherits from"""


import uuid
from datetime import datetime
from . import storage


class BaseModel:
    """This defines all common attributes or methods for other classes"""
    def __init__(self, *args, **kwargs):
        """Initialises the object when created"""
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'updated_at' or key == 'created_at':
                    self.__dict__[key] = datetime.fromisoformat(value)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Called when the print command is recieved"""
        return ("[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.to_dict()))

    def __repr__(self):
        """Also called when a print command is received"""
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                self.id, self.to_dict()))

    def save(self):
        """Updates the public instance attribute updated_at
        with the current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returs a dictionary containing all keys/values of __dict__"""
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return (dictionary)
