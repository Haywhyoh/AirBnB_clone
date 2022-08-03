#!/usr/bin/python3
from curses import setupterm
from sys import settrace
import json
from os.path import exists
class FileStorage:

    __file_path = "file.json"
    __objects = {}
    # def __init__(self, file_path, object):
    #     self.__file_path = file_path
    #     self.__

    # @property
    # def get_file_path(self):
    #     return self.__file_path
    
    # @set_file_path.setter
    # def set_file_path(self, file_path):
    #     self.__file_path = file_path
    
    # @property
    # def get_object(self, object)

    def all(self):
        return self.__objects
    def new(self, obj):
        if obj:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id )
            FileStorage.__objects[key] = obj
    def reload(self):
        from models.base_model import BaseModel
        class_dict = {"BaseModel" : BaseModel}
        if exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as fp:
                new_dict = json.load(fp)
                for key, value in new_dict.items():
                    self.new(class_dict[value['__class__']](**value))
        
    def save(self):
        dict = {}
        for key, value in FileStorage.__objects.items():
            dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as fp:
            json.dump(dict, fp)

