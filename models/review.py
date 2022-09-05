#!/usr/bin/python3
"""This gives the reviews on the apartment"""

from models.base_model import BaseModel


class Review(BaseModel):
    """This inherits from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
