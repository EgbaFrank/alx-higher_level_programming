#!/usr/bin/python3
"""
Contains testcases for the rectangle class
"""
import doctest
import unittest
from models.base import Base
from models.rectangle import Rectangle


class Testcase(unittest.TestCase):
    """Test cases for the rectangle class"""
    def test_docstr(self):
        """Checks for docstring"""
        mod_docstr_len = len(Rectangle.__module__.__doc__)
        cls_docstr_len = len(Rectangle.__doc__)
        func_docstr_len = len(Rectangle.__init__.__doc__)
        self.assertTrue(mod_docstr_len > 1)
        self.assertTrue(cls_docstr_len > 1)
        self.assertTrue(func_docstr_len > 1)

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
            rect2 = Rectangle(0, 8)
        with self.assertRaises(ValueError):
            rect2 = Rectangle(4, 0)
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
        rect3 = Rectangle(5, 6)

        with self.assertRaises(TypeError):
            rect3.display("Test")

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

        rect1.update(id=5)
        self.assertEqual(rect1.id, 5)

        rect1.update(width=12)
        self.assertEqual(rect1.width, 12)

        rect1.update(x=14, height=15, y=13)
        self.assertEqual(rect1.height, 15)
        self.assertEqual(rect1.x, 14)
        self.assertEqual(rect1.y, 13)

        # Error check
        with self.assertRaises(TypeError):
            rect1.update()

        with self.assertRaises(TypeError):
            rect1.update(1, 2, 3, 4, 5, 6)

        with self.assertRaises(TypeError):
            rect1.update(None)

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
        Rectangle.save_to_file([])

        with open("Rectangle.json") as file:
            j_str = file.read()

        self.assertEqual(j_str, '[]')

        # Check for None
        Rectangle.save_to_file(None)

        with open("Rectangle.json") as file:
            j_str = file.read()

        self.assertEqual(j_str, '[]')

        # Check for empty list
        with open("Rectangle.json") as file:
            j_str = file.read()

        self.assertEqual(j_str, '[]')

        # Check for instance
        r1 = Rectangle(10, 7, 2, 8, 19)
        r2 = Rectangle(2, 4)

        r2.update(20)

        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json") as file:
            j_str = file.read()

        self.assertEqual(j_str,
                         ('[{"id": 19, "width": 10, '
                          '"height": 7, "x": 2, "y": 8}, '
                          '{"id": 20, "width": 2, '
                          '"height": 4, "x": 0, "y": 0}]'))

    def test_from_json_str(self):
        """Test cases for the from_json_string method"""
        # Setting up instances
        rect4 = Rectangle(3, 4)
        rect5 = Rectangle(5, 6)

        rect4.update(1)
        rect5.update(2)

        rd4 = rect4.to_dictionary()
        rd5 = rect5.to_dictionary()
        input_str = Rectangle.to_json_string([rd4, rd5])
        output_str = Rectangle.from_json_string(input_str)

        # Validating output
        self.assertEqual([rd4, rd5], [
            {'id': 1, 'width': 3, 'height': 4, 'x': 0, 'y': 0},
            {'id': 2, 'width': 5, 'height': 6, 'x': 0, 'y': 0}
        ])

        self.assertEqual(input_str,
                         ('[{"id": 1, "width": 3, '
                          '"height": 4, "x": 0, "y": 0}, '
                          '{"id": 2, "width": 5, '
                          '"height": 6, "x": 0, "y": 0}]'))

        self.assertEqual(output_str, [
            {'id': 1, 'width': 3, 'height': 4, 'x': 0, 'y': 0},
            {'id': 2, 'width': 5, 'height': 6, 'x': 0, 'y': 0}
        ])

        self.assertIsInstance(input_str, str)
        self.assertIsInstance(output_str, list)

    def test_create(self):
        """Test cases for the create method"""

        # Checking error cases
        with self.assertRaises(TypeError):
            r1 = Rectangle(3, 5, 1)
            r1_dictionary = r1.to_dictionary()
            r2 = Rectangle.create({})

        with self.assertRaises(TypeError):
            r1 = Rectangle(3, 5, 1)
            r1_dictionary = r1.to_dictionary()
            r2 = Rectangle.create(None)

        # Rectangle create test
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)

        self.assertFalse(r2 == r1)
        self.assertFalse(r2 is r1)
        self.assertEqual(str(r1), str(r2))

        r3 = Rectangle(1, 2, 3, 4, 5)
        r3_dictionary = r3.to_dictionary()
        r2 = Rectangle.create(**r3_dictionary)

        self.assertFalse(r2 == r3)
        self.assertFalse(r2 is r3)
        self.assertEqual(str(r2), str(r3))

        # Square create test

    def test_load_from_file(self):
        """Test cases for the load_from_file method"""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        list_rectangle_input = [r1, r2]

        Rectangle.save_to_file(list_rectangle_input)

        list_rectangle_output = Rectangle.load_from_file()

        self.assertEqual(str(list_rectangle_output[0]),
                         '[Rectangle] (1) 2/8 - 10/7')
        self.assertEqual(str(list_rectangle_output[1]),
                         '[Rectangle] (2) 0/0 - 2/4')
        self.assertNotEqual(id(list_rectangle_output[0]),
                            id(list_rectangle_output[1]))
        self.assertNotEqual(id(list_rectangle_input[0]),
                            id(list_rectangle_output[0]))
        self.assertNotEqual(id(list_rectangle_input[1]),
                            id(list_rectangle_output[1]))

    def test_save_to_csv(self):
        """Test cases for the save_to_csv method"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]


        Rectangle.save_to_file_csv(list_rectangles_input)

        # Add None test
        Rectangle.save_to_file_csv(None)
        # Add read test

    def test_load_from_file_csv(self):
        """Test cases for the load from file csv method"""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        list_rectangles_input = [r1, r2]


        Rectangle.save_to_file_csv(list_rectangles_input)
        list_rectangle_output = Rectangle.load_from_file_csv()

        self.assertEqual(str(list_rectangle_output[0]), "[Rectangle] (1) 2/8 - 10/7")
        self.assertEqual(str(list_rectangle_output[1]), "[Rectangle] (2) 0/0 - 2/4")


if __name__ == "__main__":
    unittest.main()
