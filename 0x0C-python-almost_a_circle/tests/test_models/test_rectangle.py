#!/usr/bin/python3
"""
Contains testcases for the rectangle class
"""
import doctest
import unittest
from models.base import Base
from models.rectangle import Rectangle

class Testcase(unittest.TestCase):
    # Add a docstring test

    def test_inheritence(self):
        """Test for inheritence and class type"""
        rect1 = Rectangle(5, 4)

        self.assertIsInstance(rect1, Rectangle)
        self.assertTrue(issubclass(type(rect1), Base))

    def test_attr(self):
        """Validate attributes"""
        rect1 = Rectangle(5, 3)

        self.assertEqual(rect1.width, 5)
        self.assertEqual(rect1.height, 3)
        self.assertEqual(rect1.x, 0)
        self.assertEqual(rect1.y, 0)
        self.assertIsNotNone(rect1.id)

        rect3 = Rectangle(5, 3, 2, 7, 8)

        self.assertEqual(rect3.id, 8)

    def test_arg_count(self):
        """Checks argument counts"""
        with self.assertRaises(TypeError):
            rect2 = Rectangle()

        with self.assertRaises(TypeError):
            rect2 = Rectangle(1, 2, 2, 1, 7, 4)

    def test_arg_type(self):
        """Check argument type"""
        with self.assertRaises(TypeError):
            rect2 = Rectangle("Test", 6)

        with self.assertRaises(TypeError):
            rect2 = Rectangle(4, "Test")

        with self.assertRaises(TypeError):
            rect2 = Rectangle(2, 3, "Test")

        with self.assertRaises(TypeError):
            rect2 = Rectangle(1, 3, 4, "Test")

        with self.assertRaises(TypeError):
            rect2 = Rectangle(True, 3)

        """Check negatives"""
        with self.assertRaises(ValueError):
            rect2 = Rectangle(-3, 6)
        with self.assertRaises(ValueError):
            rect2 = Rectangle(2, -9)
        with self.assertRaises(ValueError):
            rect2 = Rectangle(3, 4, -6)
        with self.assertRaises(ValueError):
            rect2 = Rectangle(5, 6, 7, -3)

        """Check Attributes"""
        rect3 = Rectangle(5, 6)
        with self.assertRaises(AttributeError):
            rect3 = Rectangle.__width
        with self.assertRaises(AttributeError):
            rect3 = Rectangle.__x

    def test_area(self):
        """Tests the area of the rectangle instance"""
        rect3 = Rectangle(5, 6)
        self.assertEqual(rect3.area(), 30)

    def test_display(self):
        """Test the rectangle print out via doctest"""
        doctest.run_docstring_examples(Rectangle.display, globals())

    def test_print(self):
        """Test print override"""
        rect4 = Rectangle(2, 3, 0, 0, 5)

        self.assertEqual(str(rect4), "[Rectangle] (5) 0/0 - 2/3")

    def test_update(self):
        """Testing the update function"""
        rect1 = Rectangle(10, 10, 10, 10)

        rect1.update(75)
        self.assertEqual(rect1.id, 75)
        rect1.update(75, 5)
        self.assertEqual(rect1.width, 5)
        rect1.update(75, 5, 3)
        self.assertEqual(rect1.height, 3)
        rect1.update(75, 5, 3, 4)
        self.assertEqual(rect1.x, 4)
        rect1.update(75, 5, 3, 4, 2)
        self.assertEqual(rect1.y, 2)
        rect1.update(id = 5)
        self.assertEqual(rect1.id, 5)
        rect1.update(width = 12)
        self.assertEqual(rect1.width, 12)
        rect1.update(x = 14, height = 15, y = 13)
        self.assertEqual(rect1.height, 15)
        self.assertEqual(rect1.x, 14)
        self.assertEqual(rect1.y, 13)

        # Error check
        with self.assertRaises(TypeError):
            rect1.update()

        with self.assertRaises(TypeError):
            rect1.update(1, 2, 3, 4, 5, 6)

    def test_to_dict(self):
        """Test cases for the to_dictionary method"""
        rect = Rectangle(5, 3, 2, 2, 34)
        rect2 = Rectangle(1, 1, 0, 0, 3)

        self.assertEqual(str(rect), "[Rectangle] (34) 2/2 - 5/3")
        self.assertEqual(str(rect2), "[Rectangle] (3) 0/0 - 1/1")

        rect_dict = rect.to_dictionary()
        self.assertIsInstance(rect_dict, dict)

        rect2.update(**rect_dict)
        self.assertEqual(str(rect2), "[Rectangle] (34) 2/2 - 5/3")

        doctest.run_docstring_examples(Rectangle.to_dictionary, globals())

    def test_to_json_string(self):
        """Test cases for the to_json_string method"""
        # Success cases
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertIsInstance(dictionary, dict)
        self.assertIsInstance(json_dictionary, str)

        with self.assertRaises(TypeError):
            json_dictionary = Base.to_json_string()

        doctest.run_docstring_examples(Rectangle.to_json_string, globals())

    def test_save_to_json(self):
        """Test cases for the save_to_json method"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

if __name__ == "__main__":
    unittest.main()
