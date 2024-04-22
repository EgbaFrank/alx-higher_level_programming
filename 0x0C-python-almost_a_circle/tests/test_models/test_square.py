#!/usr/bin/python3
"""
Contains Tests for the Square class
"""
import doctest
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class Testcase(unittest.TestCase):
    """Runs the test for the square class"""
    # Add test for docstr

    def test_inheritence(self):
        """Test for inheritence and class type"""
        sq1 = Square(5)

        self.assertIsInstance(sq1, Square)
        self.assertTrue(issubclass(type(sq1), Base))
        self.assertTrue(issubclass(type(sq1), Rectangle))

    def test_attr(self):
        """Validate attributes"""
        sq1 = Square(5)

        self.assertEqual(sq1.size, 5)
        self.assertEqual(sq1.x, 0)
        self.assertEqual(sq1.y, 0)
        self.assertIsNotNone(sq1.id)

        sq3 = Square(5, 2, 7, 8)
        sq3.size = 25

        self.assertEqual(sq3.id, 8)
        self.assertEqual(sq3.size, 25)
        self.assertEqual(str(sq3), "[Square] (8) 2/7 - 25")

    def test_arg_count(self):
        """Checks argument counts"""
        with self.assertRaises(TypeError):
            sq2 = Square()

        with self.assertRaises(TypeError):
            sq2 = Square(1, 2, 2, 1, 7)

    def test_TypeErrors(self):
        """Tests arguments for TypeError"""
        with self.assertRaises(TypeError):
            sq3 = Square('t')

        with self.assertRaises(ValueError):
            sq3 = Square(-7)

    def test_update_func(self):
        """Testcase for the update function"""
        sq = Square(5)

        """Success case checks"""
        # Check for args
        sq.update(2, 3, 4, 5)
        self.assertEqual(sq.id, 2)
        self.assertEqual(sq.size, 3)
        self.assertEqual(sq.x, 4)
        self.assertEqual(sq.y, 5)

        # Checks for kwargs
        sq.update(id = 15, size = 35, x = 4, y = 23)
        self.assertEqual(sq.id, 15)
        self.assertEqual(sq.size, 35)
        self.assertEqual(sq.x, 4)
        self.assertEqual(sq.y, 23)

        # Check both
        sq.update(3, 4, x=65, y=45)
        self.assertEqual(sq.id, 3)
        self.assertEqual(sq.size, 4)
        self.assertEqual(sq.x, 4)
        self.assertEqual(sq.y, 23)

    def test_to_dict(self):
        """Test cases for the to_dictionary method"""
        sq = Square(5, 2, 2, 34)
        sq2 = Square(1, 0, 0, 3)

        self.assertEqual(str(sq), "[Square] (34) 2/2 - 5")
        self.assertEqual(str(sq2), "[Square] (3) 0/0 - 1")

        sq_dict = sq.to_dictionary()
        self.assertIsInstance(sq_dict, dict)

        sq2.update(**sq_dict)
        self.assertEqual(str(sq2), "[Square] (34) 2/2 - 5")

        doctest.run_docstring_examples(Square.to_dictionary, globals())

if __name__ == "__main__":
    unittest.main()
