#!/usr/bin/python3
from curses import setupterm
from sys import settrace
from models.base_model import BaseModel
import json
from os.path import exists
class FileStorage(BaseModel):

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
            key = '{} {}'.format(obj.__class__.__name__, obj.id )
            FileStorage.__objects[key] = obj
    def reload(self):
        if exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as fp:
                for key, value in json.load(fp).items():
                    my_dict = {}
                    my_dict[key] = value.to_dict()
            FileStorage.__objects = my_dict
        
    def save(self):
        dict = {}
        for key, value in FileStorage.__objects.items():
            dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as fp:
            json.dump(dict, fp)
