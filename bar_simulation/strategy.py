#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Based in parts on:
# https://github.com/JamesTeague/ElFarolBarCapstone/blob/master/Strategy.py


import random


class Strategies():
    """Class to hold the strategy (information) every person has.

    Parameters
    ----------
    :param id: int
        Id of the person. Can be used as an identifier.
    """

    def __init__(self):
        self.create_strategies(Strategies.attendance_list)

    @staticmethod
    def create_strategies(self, attendance_list):
        pass

    def get_strategy():
        return ...


class NaiveStrategy():
    """docstring for NaiveStrategy."""

    def __init__(self):
        super().__init__()

    def get_strategy(self):
        """Create an instance of class Strategies.
        """
        pass

    def make_decision(self):
        return int(2 * random.uniform(0, 1))


class ArthurStrategy():
    """docstring for ArthurStrategy."""

    def __init__(self):
        super().__init__()
        self.get_strategy_set()

    def get_strategy_set(self):
        """Create an instance of class Strategies and get 3 strategies.
        """
        self.own_strategies = []
        strategies = Strategies()
        self.own_strategies.append(strategies.get_strategies())


class BellSetharesStrategy():
    """docstring for BellSetharesStrategy."""

    def __init__(self):
        super().__init__()
