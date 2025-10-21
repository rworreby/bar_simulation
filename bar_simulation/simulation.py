#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Simulation():
    """Class to run the evolution of bar visits over a course of weeks.

    Parameters
    ----------
    :param n_weeks: int
        Number of weeks to simulate.
    """

    def __init__(self, config=None):
        self.duration = config.duration
        self.output_dir = config.output_dir
        self.strategy = config.strategy
        self.past_attendence = config.past_attendenece

    def __str__(self) -> str:
        return f"Simulation Parameters: \n\
            Simulation duration: {self.duration}, \n\
            Output dir: {self.output_dir}, \n\
            Strategy: {self.strategy}, \n\
            Past attendence: {self.past_attendence}"

    @classmethod
    def get_num_weeks(cls):
        """Returns number of weeks the simulation runs for."""
        return cls.n_weeks
