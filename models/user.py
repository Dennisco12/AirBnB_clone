#!/usr/bin/python3
""" This defines the information of the the user"""
from models.base_model import BaseModel


class User(BaseModel):
    """This inherits from basemodel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
