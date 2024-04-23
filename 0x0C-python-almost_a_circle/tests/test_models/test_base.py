#!/usr/bin/python3
"""
Contains test cases for the base class
"""
from models.base import Base
import unittest


class TestBase(unittest.TestCase):
    """ Test cases for base class """
    def test_docstr(self):
        """Checks for docstring"""
        mod_docstr_len = len(Base.__module__.__doc__)
        cls_docstr_len = len(Base.__doc__)
        func_docstr_len = len(Base.__init__.__doc__)
        self.assertTrue(mod_docstr_len > 1)
        self.assertTrue(cls_docstr_len > 1)
        self.assertTrue(func_docstr_len > 1)

    def test_success(self):
        """Checks success cases"""
        base1 = Base()
        base2 = Base()
        base3 = Base(12)
        base4 = Base()

        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)
        self.assertEqual(base3.id, 12)
        self.assertEqual(base4.id, 3)

    def test_error(self):
        """Check error cases"""
        self.assertRaises(TypeError, Base, 1, 2,)


if __name__ == "__main__":
    unittest.main()
