#!/usr/bin/python3
from curses import setupterm
from sys import settrace
from models.base_model import BaseModel
import json
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
            self.__objects[key] = obj
    def reload(self):
        if __file_path:
            try:
                with open(self.__file_path, 'r') as fp:
                    self.__objects = json.load(fp)

            except:
                    pass
    def save(self):
        with open(self.__file_path, 'w+') as fp:
            json.dump(self.__objects, fp)
