#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Person():
    """Class to represent a person (i.e. bargoer).

    Parameters
    ----------
    :param id: int
        Id of the person. Can be used as an identifier.
    """
    # Number of the instances of class Person
    id_number = 0

    def __init__(self):
        Person.id_number += 1
        self.id = Person.id_number

    def __str__(self) -> str:
        return f"Person ID: {self.id}"

    @classmethod
    def get_num_instances(cls):
        """Returns number of instances of class."""
        return cls.id_number