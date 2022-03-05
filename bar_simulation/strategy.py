#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Based in parts on:
# https://github.com/JamesTeague/ElFarolBarCapstone/blob/master/Strategy.py

class Strategies():
    """Class to hold the strategy (information) every person has.

    Parameters
    ----------
    :param id: int
        Id of the person. Can be used as an identifier.
    """
    attendance_list = [44, 78, 56, 15, 23, 67, 84, 34, 45, 76, 40, 56,
                       22, 35]

    def __init__(self):
        self.create_strategies(Strategies.attendance_list)

    @staticmethod
    def create_strategies(self, attendance_list):
        pass

    def get_strategies():
        return ...


class ArthurStrategy():
    """docstring for ArthurStrategy."""

    def __init__(self):
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
