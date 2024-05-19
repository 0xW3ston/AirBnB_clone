#!/usr/bin/python3
""" This file is for fs engine """
import json
import os
from models.base_model import BaseModel
from models.amenity import Amenity
from models.state import State
from models.city import City
from models.review import Review
from models.user import User
from models.place import Place
# from models.base_model import BaseModel #avoid circular


class FileStorage:
    """ This class is for FileStorage """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ This method is for all """
        return FileStorage.__objects

    def new(self, obj):
        """ This method is for new """
        id = obj.to_dict()["id"]
        className = obj.to_dict()["__class__"]
        keyName = className+"."+id
        FileStorage.__objects[keyName] = obj

    def save(self):
        """ This method is for save """
        filepath = FileStorage.__file_path
        data = dict(FileStorage.__objects)
        for key, value in data.items():
            data[key] = value.to_dict()
        with open(filepath, 'w') as f:
            json.dump(data, f)

    def reload(self):
        """ This method is for reload """
        filepath = FileStorage.__file_path
        data = FileStorage.__objects
        if os.path.exists(filepath):
            try:
                with open(filepath) as f:
                    for key, value in json.load(f).items():
                        if "BaseModel" in key:
                            data[key] = BaseModel(**value)
                        if "Amenity" in key:
                            data[key] = Amenity(**value)
                        if "Review" in key:
                            data[key] = Review(**value)
                        if "City" in key:
                            data[key] = City(**value)
                        if "Place" in key:
                            data[key] = Place(**value)
                        if "State" in key:
                            data[key] = State(**value)
                        if "User" in key:
                            data[key] = User(**value)
            except Exception:
                pass
