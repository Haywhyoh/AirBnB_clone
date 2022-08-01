#!/usr/bin/python3
import uuid
from datetime import datetime

class BaseModel():

    def __init__(self):
        self.id = uuid.uuid4()
        self.createdat = datetime.now().isoformat()
        self.updatedat = datetime.now().isoformat()
    
    def __str__(self):
        return f'[{self.__class__}] ({self.id}) <{self.__dict__}>'

    def save(self):
        

    def to_dict(save):
