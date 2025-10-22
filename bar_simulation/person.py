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

    def __init__(self, strategy=None):
        Person.id_number += 1
        self.id = Person.id_number
        self.strategy_name = strategy
        self.attendence = []

        if self.strategy_name == "arthur":
            from bar_simulation.strategy import ArthurStrategy
            self.strategy = ArthurStrategy()
        elif self.strategy_name == "naive":
            from bar_simulation.strategy import NaiveStrategy
            self.strategy = NaiveStrategy()
        elif self.strategy_name == "bell":
            from bar_simulation.strategy import BellSetharesStrategy
            self.strategy = BellSetharesStrategy()
        else:
            from bar_simulation.strategy import NaiveStrategy
            self.strategy = NaiveStrategy()

    def __str__(self) -> str:
        return f"Person ID: {self.id}"

    @classmethod
    def get_max_id_instances(cls):
        """Returns current id number of new instances of class."""
        return cls.id_number
