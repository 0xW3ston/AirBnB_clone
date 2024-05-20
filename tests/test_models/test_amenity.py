#!/usr/bin/python3
""" utest for Amenity """
import unittest
from models.amenity import Amenity
from datetime import datetime


class CityTestCase(unittest.TestCase):
    """ class for amenity test """

    def test_amenity(self):
        """ test for existence """
        new = Amenity()
        self.assertTrue(hasattr(new, "id"))
        self.assertTrue(hasattr(new, "created_at"))
        self.assertTrue(hasattr(new, "updated_at"))
        self.assertTrue(hasattr(new, "name"))

        """ datatype test """
        self.assertIsInstance(new.id, str)
        self.assertIsInstance(new.created_at, datetime)
        self.assertIsInstance(new.updated_at, datetime)
        self.assertIsInstance(new.name, str)


if __name__ == '__main__':
    unittest.main()
