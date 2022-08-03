#!/usr/bin/python3
from curses import setupterm
from sys import settrace
from models.base_model import BaseModel
import json
class FileStorage(BaseModel):

    def __init__(self):
        self.file_path = file_path

    @property
    def file_path(self):
        return self.__file_path
    
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
        pass
    def save(self):
        pass
