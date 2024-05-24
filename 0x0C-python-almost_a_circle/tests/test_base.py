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

    def test_auto_id_add1(self):
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


class TestBase_create(unittest.TestCase):
    """Tests create method of Base class"""

    def testRect_create_with_id(self):
        r = Rectangle(1, 2)
        new = r.create(**{ 'id': 80 })
        self.assertEqual(80, new.id)

    def testRect_create_with_width(self):
        r = Rectangle(1, 2)
        new = r.create(**{ 'id': 80, 'width': 4 })
        self.assertEqual(4, new.width)

    def testRect_create_with_height(self):
        r = Rectangle(1, 2)
        new = r.create(**{ 'id': 80, 'width': 4, 'height': 6 })
        self.assertEqual(6, new.height)

    def testRect_create_with_x(self):
        r = Rectangle(1, 2)
        new = r.create(**{ 'id': 80, 'width': 4, 'height': 6, 'x': 2 })
        self.assertEqual(2, new.x)

    def testRect_create_with_y(self):
        r = Rectangle(1, 2)
        new = r.create(**{ 'id': 80, 'width': 4, 'height': 6, 'x': 2, 'y': 2 })
        self.assertEqual(2, new.y)

    def testSqr_create_with_id(self):
        s = Square(2)
        new = s.create(**{ 'id': 80 })
        self.assertEqual(80, new.id)

    def testSqr_create_with_size(self):
        s = Square(2)
        new = s.create(**{ 'id': 80, 'size': 4 })
        self.assertEqual(4, new.size)

    def testSqr_create_with_x(self):
        s = Square(2)
        new = s.create(**{ 'id': 80, 'size': 4, 'x': 2 })
        self.assertEqual(2, new.x)

    def testSqr_create_with_y(self):
        s = Square(2)
        new = s.create(**{ 'id': 80, 'size': 4, 'x': 2, 'y': 2 })
        self.assertEqual(2, new.y)

class TestBase_save_to_file(unittest.TestCase):
    """Tests save_to_file method of Base class"""

    def testRect_save_to_file_none(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())

    def testRect_save_to_file_empty(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())

    def testRect_save_to_file_obj(self):
        r = Rectangle(2, 3, 0, 0, 4)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertEqual('[{"id": 4, "width": 2, "height": 3, "x": 0, "y": 0}]', f.read())

    def testSqr_save_to_file_none(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def testSqr_save_to_file_empty(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def testSqr_save_to_file_obj(self):
        r = Square(2, 0, 0, 4)
        Square.save_to_file([r])
        with open("Square.json", "r") as f:
            self.assertEqual('[{"id": 4, "size": 2, "x": 0, "y": 0}]', f.read())


class TestBase_load_from_file(unittest.TestCase):
    """Tests load_from_file method of Base class"""

    def testRect_load_from_file_nofile(self):
        output = Rectangle.load_from_file()
        self.assertEqual([], output)
    
    def testRect_load_from_file_withfile(self):
        r = Rectangle(2, 3, 0, 0, 4)
        Rectangle.save_to_file([r])
        output = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def testSqr_load_from_file_nofile(self):
        output = Square.load_from_file()
        self.assertEqual([], output)

    def testSqr_load_from_file_withfile(self):
        s = Square(2, 0, 0, 4)
        Square.save_to_file([s])
        output = Square.load_from_file()
        self.assertTrue(all(type(obj) == Square for obj in output))


if __name__ == '__main__':
    unittest.main()
