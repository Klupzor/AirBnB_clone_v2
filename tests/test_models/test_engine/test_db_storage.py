#!/usr/bin/python3
"""test for file storage"""
import unittest
import pep8
import json
import os
import sys
import MySQLdb
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.db_storage import DBStorage


class TestDBStorage(unittest.TestCase):
    '''this will test the FileStorage'''

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        user_name = os.environ.get('HBNB_MYSQL_USER')
        password = os.environ.get('HBNB_MYSQL_PWD')
        database_name = os.environ.get('HBNB_MYSQL_DB')
        host_name = os.environ.get('HBNB_MYSQL_HOST')

        db = MySQLdb.connect(
            host=host_name,
            user=user_name,
            passwd=password,
            db=database_name)

        cur = db.cursor()

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        cur.close()

    def test_pep8_DBStorage(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")
