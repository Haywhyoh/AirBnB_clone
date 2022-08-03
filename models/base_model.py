#!/usr/bin/python3

"""
This module holds the class (BaseModel) that defines the
common attributes or methods for other classes
"""
import uuid
from datetime import datetime as dt
from models import storage

class BaseModel():
    """
    BaseModel class (or object) defines the common attributes
    or methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        The __init__ method lets the class (BaseModel)
        initialize the object's attributes
        """
        if kwargs:
            for key, value in kwargs.items():
                fdate = "%Y-%m-%dT%H:%M:%S.%f"
                if 'updated_at' == key:
                    self.updated_at = dt.strptime(kwargs["updated_at"], fdate)
                elif 'created_at' == key:
                    self.created_at = dt.strptime(kwargs["created_at"], fdate)
                elif '__class__' == key:
                    pass
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = dt.now()
            self.updated_at = dt.now()
            storage.new(self)

    def __str__(self):
        """
        The __str__ method represents the class objects as strings
        """
        class_name = self.__class__.__name__
        return '[{}] ({}) <{}>'.format(class_name, self.id, self.__dict__)

    def save(self):
        """
        The save method updates the public instance attribute (updated_at)
        with the current datetime
        """
        self.updated_at = dt.now()
        storage.save()

    def to_dict(self):
        """
        The to_dict method returns a dictionary
        containing all key or values of __dict__of the instance
        """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict