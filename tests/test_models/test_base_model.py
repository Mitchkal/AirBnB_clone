#!/usr/bin/python3

"""
module test_base_models
tests the basemodel class
"""

import os
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def test_init(self):
        self.assertTrue(isinstance(self.base1, BaseModel))

    def test_attributes(self):
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))
        self.assertTrue(hasattr(BaseModel, "save"))

    def test_functions(self):
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_save(self):
        self.base1.save()
        self.assertNotEqual(self.base1.created_at, self.base1.updated_at)


    def test_to_dict(self):
        base1_dict = self.base1.to_dict()
        self.assertIsinstance(base1_dict['created_at'], str)
        self.assertIsinstance(base1_dict['updated_at'], str)
        self.assertEqual(self.base1.__class__.__name__, 'BaseModel')

if __name__ == "__main__":
    unittest.main()

