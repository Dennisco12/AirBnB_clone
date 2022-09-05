#!/usr/bin/python3
"""This recreates a BaseModel from another one by using a dictionary
reresentation"""

import json


class FileStorage:
    """This serializes instances to a JSON file and deserializes
    JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary objects"""
        return type(self).__objects

    def new(self, obj):
        """Sets in objects the obj with key id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """This serializes objects to JSON file"""
        json_dict = {}
        for key, value in type(self).__objects.items():
            json_dict[key] = value.to_dict()
        with open(type(self).__file_path, 'w', encoding='utf-8') as f:
            json.dump(json_dict, f)

    def reload(self):
        """Deserialises the JSON file to __objects"""
        new_obj = {}
        try:
            with open(type(self).__file_path, encoding='utf-8') as f:
                new_obj = json.load(f)
        except Exception:
            pass
        else:
            from models.base_model import BaseModel
            from models.user import User
            from models.place import Place
            from models.state import State
            from models.review import Review
            from models.amenity import Amenity
            from models.city import City
            for key, value in new_obj.items():
                if "BaseModel" in key.split("."):
                    type(self).__objects[key] = BaseModel(**value)
                elif "User" in key.split("."):
                    type(self).__objects[key] = User(**value)
                elif "Place" in key.split('.'):
                    type(self).__objects[key] = Place(**value)
                elif "State" in key.split('.'):
                    type(self).__objects[key] = State(**value)
                elif "Review" in key.split('.'):
                    type(self).__objects[key] = Review(**value)
                elif "Amenity" in key.split('.'):
                    type(self).__objects[key] = Amenity(**value)
                elif "City" in key.split('.'):
                    type(self).__objects[key] = City(**value)
