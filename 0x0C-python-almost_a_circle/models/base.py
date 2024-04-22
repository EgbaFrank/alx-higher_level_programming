#!/usr/bin/python3
"""
This module contains the base class
"""
import json


class Base:
    """Base model class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        This is used to initialize new Base instances
        """
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries

        Example:
            >>> r1 = Rectangle(10, 7, 2, 8, 1)
            >>> dictionary = r1.to_dictionary()
            >>> dictionary = dict(sorted(dictionary.items()))
            >>> json_dictionary = Base.to_json_string([dictionary])
            >>> print(dictionary)
            {'height': 7, 'id': 1, 'width': 10, 'x': 2, 'y': 8}
            >>> print(type(dictionary))
            <class 'dict'>
            >>> print(json_dictionary)
            [{"height": 7, "id": 1, "width": 10, "x": 2, "y": 8}]
            >>> print(type(json_dictionary))
            <class 'str'>
            >>> json_dict2 = Base.to_json_string([])
            >>> print(json_dict2)
            []
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = f"{cls.__name__}.json"

        with open(filename, 'w', encoding="utf-8") as file:
            json_list = [obj.to_dictionary for obj in list_objs]
            file.write(cls.to_json_string(json_list))
