#!/usr/bin/python3
""" This file is for user """
from models.base_model import BaseModel


class User(BaseModel):
    """ This class is for User """
    first_name = ""
    last_name = ""
    email = ""
    password = ""
