#!/usr/bin/python3
"""Defines unit tests for base class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_instantiation(unittest.TestCase):
    """Testing instantiation of Base class"""

    def test_auto_id(self):
        b = Base()
        self.assertEqual(b.id, 1)

    def test_auto_id_add_1(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_unique_id(self):
        b = Base(3)
        self.assertEqual(b.id, 3)


class TestBase_to_json_string(unittest.TestCase):
    """Tests to_json_string method of Base class"""

    def test_to_json_string_none(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty_list(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_one_dict(self):
        string = Base.to_json_string([ {"id": 3} ])
        self.assertEqual('[{"id": 3}]', string)

    def test_to_json_string_return_str(self):
        string = Base.to_json_string([ {"id": 3} ])
        self.assertEqual(str, type(string))


class TestBase_from_json_string(unittest.TestCase):
    """Tests from_json_string method of Base class"""

    def test_from_json_string_none(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty_string(self):
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_string(self):
        list_dict = Base.from_json_string('[ {"id": 3} ]')
        self.assertEqual(list_dict, [{"id": 3}])

    def test_from_json_string_return_list(self):
        list_dict = Base.from_json_string('[ {"id": 3} ]')
        self.assertEqual(type(list_dict), list)





if __name__ == '__main__':
    unittest.main()
