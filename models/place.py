#!/usr/bin/python3
"""This module holds the Place object"""
from models.base_model import BaseModel


class Place(BaseModel):
    """This is the class of the Place object"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    longititude = 0.0
    latitude = 0.0
    amenity_ids = []
