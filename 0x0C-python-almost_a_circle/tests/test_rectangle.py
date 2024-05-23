#!/usr/bin/python3

"""Defines unit tests for Rectangle class"""
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle_instantiation(unittest.TestCase):
    """Testing instantiation of Rectangle class"""

    def test_two_args(self):
        r1 = Rectangle(2, 3)
        r2 = Rectangle(4, 6)
        self.assertEqual(r1.id, r2.id - 1)

    def test_three_args(self):
        r = Rectangle(2, 4, 1)
        self.assertEqual(r.x, 1)

    def test_four_args(self):
        r = Rectangle(3, 4, 1, 2)
        self.assertEqual(r.y, 2)

    def test_string_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("2", 3)

    def test_string_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, "3")

    def test_string_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 3, "1")

    def test_string_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 3, 1, "2")

    def test_five_args(self):
        r = Rectangle(2, 3, 1, 2, 5)
        self.assertEqual(r.id, 5)

    def test_neg_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-2, 4)

    def test_neg_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, -4)
    
    def test_zero_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 4)

    def test_zero_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, 0)

    def test_neg_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(2, 4, -6)

    def test_neg_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(2, 4, 6, -3)


class TestRectangle_area(unittest.TestCase):
    """Tests area method of Rectangle class"""

    def test_area(self):
        r = Rectangle(2, 6)
        self.assertEqual(r.area(), 12)


class TestRectangle_str(unittest.TestCase):
    """Tests __str__ method of Rectangle class"""
    
    def test_str__(self):
        r = Rectangle(2, 4, 1, 2, 4)
        message = "[Rectangle] (4) 1/2 - 2/4"
        self.assertEqual(r.__str__(), message)


class TestRectangle_display(unittest.TestCase):
    """Test update method of Rectangle class"""
    
    @staticmethod
    def capture_stdout(obj):
        capture = io.StringIO()
        sys.stdout = capture
        obj.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_display_no_xy(self):
        r = Rectangle(2, 3)
        output = TestRectangle_display.capture_stdout(r)
        self.assertEqual("##\n##\n##\n", output.getvalue())

    def test_display_withx(self):
        r = Rectangle(2, 3, 1)
        output = TestRectangle_display.capture_stdout(r)
        self.assertEqual(" ##\n ##\n ##\n", output.getvalue())
    
    def test_display_withy(self):
        r = Rectangle(2, 3, 0, 1)
        output = TestRectangle_display.capture_stdout(r)
        self.assertEqual("\n##\n##\n##\n", output.getvalue())

    def test_display_withxy(self):
        r = Rectangle(2, 3, 1, 1)
        output = TestRectangle_display.capture_stdout(r)
        self.assertEqual("\n ##\n ##\n ##\n", output.getvalue())


class TestRectangle_to_dict(unittest.TestCase):
    """Tests to_dictionary method of Rectangle class"""

    def test_to_dictionary(self):
        r = Rectangle(2, 3, 1, 1, 5)
        dict_rep = {"id": 5, "width":2, "height":3, "x": 1, "y": 1}
        self.assertEqual(r.to_dictionary(), dict_rep)


class TestRectangle_update(unittest.TestCase):
    """Tests update method of Rectangle class"""

    def test_update_args_id(self):
        r = Rectangle(2, 3, 1, 1, 7)
        r.update(80)
        self.assertEqual(r.id, 80)

    def test_update_args_width(self):
        r = Rectangle(2, 3, 1, 1, 7)
        r.update(80, 4)
        self.assertEqual(r.width, 4)

    def test_update_args_height(self):
        r = Rectangle(2, 3, 1, 1, 7)
        r.update(80, 4, 6)
        self.assertEqual(r.height, 6)

    def test_update_args_x(self):
        r = Rectangle(2, 3, 1, 1, 7)
        r.update(80, 4, 6, 0)
        self.assertEqual(r.x, 0)

    def test_update_args_y(self):
        r = Rectangle(2, 3, 1, 1, 7)
        r.update(80, 4, 6, 0, 0)
        self.assertEqual(r.y, 0)

    def test_update_kwargs_id(self):
        r = Rectangle(2, 3, 1, 1, 7)
        r.update(**{ 'id':80 })
        self.assertEqual(r.id, 80)

    def test_update_kwargs_width(self):
        r = Rectangle(2, 3, 1, 1, 7)
        r.update(**{ 'id': 80, 'width': 4 })
        self.assertEqual(r.width, 4)

    def test_update_kwargs_height(self):
        r = Rectangle(2, 3, 1, 1, 7)
        r.update(**{ 'id': 80, 'width': 4, 'height': 6 })
        self.assertEqual(r.height, 6)

    def test_update_kwargs_x(self):
        r = Rectangle(2, 3, 1, 1, 7)
        r.update(**{ 'id': 80, 'width': 4, 'height': 6, 'x': 0 })
        self.assertEqual(r.x, 0)

    def test_update_kwargs_y(self):
        r = Rectangle(2, 3, 1, 1, 7)
        r.update(**{ 'id': 80, 'width': 4, 'height': 6, 'x': 0, 'y': 0 })
        self.assertEqual(r.y, 0)


if __name__ == "__main__":
    unittest.main()
