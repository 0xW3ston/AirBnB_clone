#!/usr/bin/python3
from models.base_model import BaseModel


class Place(BaseModel):
    """ This class is for Place """
    user_id = ""
    name = ""
    description = ""
    city_id = ""
    number_bathrooms = 0
    number_rooms = 0
    price_by_night = 0
    max_guest = 0
    longitude = 0.0
    latitude = 0.0
    amenity_ids = []
