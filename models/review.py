#!/usr/bin/python3
"""This module holds the Review Object"""
from models.base_model import BaseModel


class Review(BaseModel):
    """This is the class of the Review Object"""
    place_id = ""
    user_id = ""
    text = ""
