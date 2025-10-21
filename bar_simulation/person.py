#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Person():
    """Class to represent a person (i.e. bargoer).

    Parameters
    ----------
    :param id: int
        Id of the person. Can be used as an identifier.
    """
    #: Number of instances that exist of class Person
    n_inst = 0

    def __init__(self):
        super().__init__()
        Person.no_inst += 1
        self.id = Person.n_inst

    def __str__(self):
        pass

    @classmethod
    def get_num_instances(cls):
        """Returns number of instances of class."""
        return cls.n_inst

    @classmethod
    def __del__(cls):
        Person.n_inst -= 1
