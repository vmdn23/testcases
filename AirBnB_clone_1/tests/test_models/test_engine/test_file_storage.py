#!/usr/bin/python3
"""File Storage Unit Tests"""


from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import models
import os
import sys
import pep8
import unittest


class Test_FileStorage(unittest.TestCase):
    """
    Test cases for class FileStorage
    """
    def test_docstring(self):
        """Checks if docstring exist"""
        self.assertTrue(len(FileStorage.__doc__) > 1)
        self.assertTrue(len(FileStorage.all.__doc__) > 1)
        self.assertTrue(len(FileStorage.new.__doc__) > 1)
        self.assertTrue(len(FileStorage.save.__doc__) > 1)
        self.assertTrue(len(FileStorage.reload.__doc__) > 1)

    def test_pep8(self):
        """Pep8 Test"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0, "fix pep8")

    def setUp(self):
        """Sets up testing environment to not change the
        previous file storage
        """
        self.file_path = models.storage._FileStorage__file_path
        if os.path.exists(self.file_path):
            os.rename(self.file_path, 'test_storage')

    def tearDown(self):
        """Removes JSON file after test cases run """
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        if os.path.exists('test_storage'):
            os.rename('test_storage', self.file_path)

    def test_saves_new_instance(self):
        """ Tests if file is being created """
        a = BaseModel()
        models.storage.new(a)
        models.storage.save()
        file_exist = os.path.exists(self.file_path)
        self.assertTrue(file_exist)

    def test_json(self):
        """Checks for errors related to the JSON conversion"""
        with self.assertRaises(AttributeError):
            FileStorage.__objects
            FileStorage.__File_Path
