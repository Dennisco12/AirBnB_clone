#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """unittest module for testing out basemodel class"""
    def test_no_args(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_instance_stored_in_objs(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id_is_public(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at(self):
        self.assertEqual(datetime.now(), BaseModel().created_at)

    def test_unique_id(self):
        self.assertFalse(BaseModel().id, BaseModel().id)

    def test_kwargs_initialisation(self):
        value = {age : 20}
        model = BaseModel(**value)
        self.assertEqual(20, model.age)
