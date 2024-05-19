#!/usr/bin/python3
from models.base_model import BaseModel


class Review(BaseModel):
    """ This class is for Review """
    user_id = ""
    text = ""
    place_id = ""
