#!/usr/bin/python3
"""This creates a unique FileStorage instance """

from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
