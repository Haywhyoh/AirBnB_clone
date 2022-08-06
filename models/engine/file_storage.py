#!/usr/bin/python3
"""This module holds the FileStorage object"""
import json
from os.path import exists


class FileStorage:
    """
    This is the class of the FileStorage object
    which handles the serialization
    and deserialization of objects into
    or out of a local file
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns all stored objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Creates the new object to be serialized"""
        if obj:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            FileStorage.__objects[key] = obj

    def reload(self):
        """Deserialies from a local file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.place import Place
        from models.amenity import Amenity
        from models.review import Review

        class_dict = {"BaseModel": BaseModel,
                      "User": User,
                      "State": State,
                      "City": City,
                      "Place": Place,
                      "Amenity": Amenity,
                      "Review": Review}
        if exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as fp:
                new_dict = json.load(fp)
                for key, value in new_dict.items():
                    self.new(class_dict[value['__class__']](**value))

    def save(self):
        """Serializes to a local file"""
        dict = {}
        for key, value in FileStorage.__objects.items():
            dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as fp:
            json.dump(dict, fp)
