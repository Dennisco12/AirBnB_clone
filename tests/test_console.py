#!/usr/bin/python3

from unittest.mock import patch
import sys
from models.engine.file_storage import FileStorage
from models import storage
import unittest
from console import HBNBCommand
from io import StringIO

class test_command:
    """This tests the create and the show commands
    of the console.py file"""

    def test_prompt(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_create(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertLess(1, len(f.getvalue().strip()))
            key = "BaseModel.{}".format(f.getvalue().strip())
            self.assertIn(key, storage.all().keys())

    def test_show(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            ID = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            obj = storage.all()["BaseModel.{}".format(ID)]
            command = "show BaseModel {}".format(ID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), f.getvalue().strip())


if __name__ == '__main__':
    unittest.main()
