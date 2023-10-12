#!/usr/bin/python3
"""
module File storage
Handles serialization and 
deserialization for storage
"""
import json
from models.base_model import BaseModel

class FileStorage:
    """
    serialize and deserialize json
    """
    __file_path = "file.json"
    __objects = {}
    class_dict = {"BaseModel": BaseModel}

    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key
        """
        if obj:
            key = '{}.{}'.format(obj.__class__.name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """
        serialize objects to json file
        """
        _dict = {}

        for key, obj in self.__objects.items():
            if type(obj) is dict:
                _dict[key] = obj
            else:
                _dict[key] = obj.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(_dict, f)

    def reload(self):
        """
        convert Json object dictionaries to instances
        """
        try:
            with open(self.__file_path, 'r')as f:
                objs = json.load(f)

            for key, value in objs.items():
                obj = self.class_dict[val['__class__']](**val)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass
