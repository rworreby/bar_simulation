#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Simulation():
    """Class to run the evolution of bar visits over a course of weeks.

    Parameters
    ----------
    :param n_weeks: int
        Number of weeks to simulate.
    """
    #: Number of instances that exist of class Person
    n_weeks = 0

    def __init__(self):
        super().__init__()
        self.n_weeks = 100

    def __str__(self):
        pass

    @classmethod
    def get_num_weeks(cls):
        """Returns number of weeks the simulation runs for."""
        return cls.n_weeks
