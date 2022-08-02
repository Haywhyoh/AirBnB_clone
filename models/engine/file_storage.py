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
    
    @file_path.setter
    def file_path(self):
        self.__file_path = file_path