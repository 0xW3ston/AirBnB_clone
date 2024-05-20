#!/usr/bin/python3
""" utest for State """
import unittest
from models.state import State
from datetime import datetime


class StateTestCase(unittest.TestCase):
    """ class for State test """

    def test_state(self):
        """test for existence"""
        new = State()
        self.assertTrue(hasattr(new, "id"))
        self.assertTrue(hasattr(new, "created_at"))
        self.assertTrue(hasattr(new, "updated_at"))
        self.assertTrue(hasattr(new, "name"))

        """datatype test"""
        self.assertIsInstance(new.id, str)
        self.assertIsInstance(new.created_at, datetime)
        self.assertIsInstance(new.updated_at, datetime)
        self.assertIsInstance(new.name, str)


if __name__ == '__main__':
    unittest.main()
