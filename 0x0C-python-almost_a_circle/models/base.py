#!/usr/bin/python3
"""
This module contains the base class
"""
import csv
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
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            list_objs = []

        objs_dict = []

        # Validate base class inheritence

        for obj in list_objs:
            objs_dict.append(obj.to_dictionary())

        json_str = Base.to_json_string(objs_dict)

        filename = f"{cls.__name__}.json"

        with open(filename, 'w', encoding="utf-8") as file:
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        lst = []
        if json_string is None:
            return lst

        lst = json.loads(json_string)

        return lst

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)

        else:
            dummy = cls(1)

        dummy.update(**dictionary)

        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = f"{cls.__name__}.json"

        res = []

        try:
            with open(filename, encoding="utf-8") as file:
                json_data = file.read()

            if json_data:
                objs = Base.from_json_string(json_data)

                for obj in objs:
                    res.append(cls.create(**obj))
        except FileNotFoundError:
            pass

        return res

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """writes the csv string representation of list_objs to a file"""
        filename = f"{cls.__name__}.csv"

        with open(filename, "w", encoding="utf-8", newline='') as file:
            if list_objs is None:
                file.write("[]")

            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ['id', 'width', 'height', 'x', 'y']
                else:
                    fieldnames = ['id', 'size', 'x', 'y']

                csvwrite = csv.DictWriter(file, fieldnames=fieldnames)
                csvwrite.writeheader()

                for obj in list_objs:
                    csvwrite.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """reads from a csv file and creates a list of instances"""
        filename = f"{cls.__name__}.csv"

        objs_list = []

        try:
            with open(filename, encoding="utf-8", newline='') as file:
                csv_reader = csv.DictReader(file)

                for row in csv_reader:
                    # Convert value to integers
                    row = {k: int(v) for k, v in row.items()}
                    objs_list.append(cls.create(**row))

        except FileNotFoundError:
            pass

        return objs_list
