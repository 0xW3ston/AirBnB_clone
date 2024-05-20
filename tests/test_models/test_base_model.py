#!/usr/bin/python3
""" utest for Bases """
import json
import unittest
from models.base_model import BaseModel
from datetime import datetime
import models
from io import StringIO
import sys
from unittest.mock import patch
captured_output = StringIO()
sys.stdout = captured_output


class BaseModelTestCase(unittest.TestCase):
    """ class for base test """

    def setUp(self):
        """ test for base up """
        self.filepath = models.storage._FileStorage__file_path
        with open(self.filepath, 'w') as file:
            file.truncate(0)
        models.storage.all().clear()

    def tearDown(self):
        """ test for base down """
        printed_output = captured_output.getvalue()
        sys.stdout = sys.__stdout__

    def test_basemodel_init(self):
        """ test for base init """
        new = BaseModel()

        """ test for methods existence """
        self.assertTrue(hasattr(new, "__init__"))
        self.assertTrue(hasattr(new, "__str__"))
        self.assertTrue(hasattr(new, "save"))
        self.assertTrue(hasattr(new, "to_dict"))

        """test for existence"""
        self.assertTrue(hasattr(new, "id"))
        self.assertTrue(hasattr(new, "created_at"))
        self.assertTrue(hasattr(new, "updated_at"))

        """datatype test"""
        self.assertIsInstance(new.id, str)
        self.assertIsInstance(new.created_at, datetime)
        self.assertIsInstance(new.updated_at, datetime)

        """ check if saved in storage """
        keyname = "BaseModel."+new.id
        """ check if object exists by keyname """
        self.assertIn(keyname, models.storage.all())
        """ check if the object is found in storage with corr. id"""
        self.assertTrue(models.storage.all()[keyname] is new)

        """ test for update """
        new.name = "My First Model"
        new.my_number = 89
        self.assertTrue(hasattr(new, "name"))
        self.assertTrue(hasattr(new, "my_number"))
        self.assertTrue(hasattr(models.storage.all()[keyname], "name"))
        self.assertTrue(hasattr(models.storage.all()[keyname], "my_number"))

        """check if @save() update update_at timechange"""
        old_time = new.updated_at
        new.save()
        self.assertNotEqual(old_time, new.updated_at)
        self.assertGreater(new.updated_at, old_time)

        """ check if init it calls models.storage.save() """
        with patch('models.storage.save') as mock_function:
            obj = BaseModel()
            obj.save()
            mock_function.assert_called_once()

        """check if it is saved in file.json"""
        keyname = "BaseModel."+new.id
        with open(self.filepath, 'r') as file:
            saved_data = json.load(file)
        """ check if object exists by keyname """
        self.assertIn(keyname, saved_data)
        """ check if the value found in file.json is correct"""
        self.assertEqual(saved_data[keyname], new.to_dict())

    def test_basemodel_init2(self):
        """ test for base init 2 """

        new = BaseModel()
        new.name = "John"
        new.my_number = 89
        new2 = BaseModel(**new.to_dict())
        self.assertEqual(new.id, new2.id)
        self.assertEqual(new.name, "John")
        self.assertEqual(new.my_number, 89)
        self.assertEqual(new.to_dict(), new2.to_dict())

    def test_basemodel_init3(self):
        """ test for base init 3 """
        new = BaseModel()
        new2 = BaseModel(new.to_dict())
        self.assertNotEqual(new, new2)
        self.assertNotEqual(new.id, new2.id)
        self.assertTrue(isinstance(new2.created_at, datetime))
        self.assertTrue(isinstance(new2.updated_at, datetime))

        new = BaseModel()

        self.assertEqual(
            str(new),  "[BaseModel] ({}) {}".format(new.id, new.__dict__))

        old_time = new.updated_at
        new.save()
        self.assertGreater(new.updated_at, old_time)


if __name__ == '__main__':
    unittest.main()
