#!/usr/bin/python3
import uuid
from datetime import datetime

class BaseModel():

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.createdat = datetime.now()
        self.updatedat = datetime.now()

    def __str__(self):
        return '[{}] ({}) <{}>'.format(self.__class__.__name, self.id, self.__dict__)

    def save(self):
        self.updatedat = datetime.now()

    def to_dict(self):
        self.__dict__["class"] = self.__class__.__name__
        self.__dict__["createdat"] = self.createdat.isoformat()
        self.__dict__["updatedat"] = self.updatedat.isoformat()
        return self.__dict__
