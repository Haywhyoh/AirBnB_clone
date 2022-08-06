#!/usr/bin/python3
"""This module holds the User object"""
from models.base_model import BaseModel


class User(BaseModel):
    """This is the class of the User objectS"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
