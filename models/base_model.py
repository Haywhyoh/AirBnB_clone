#!/usr/bin/python3
import uuid
from datetime import datetime

class BaseModel():

    def __init__(self):
        self.id = uuid.uuid4()
        self.createdat = datetime.now()
        self.updatedat = datetime.now()
    
    