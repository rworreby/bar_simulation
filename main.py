#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse
import timeit
from bar_simulation.simulation import Simulation

"""
Bar Simulation main file.

Features:
-
"""


def parse_args(argv=None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Simulation setup parameters")
    p.add_argument("--duration", type=float, default=100, help="Simulated duration in weeks")
    p.add_argument("--output_dir", type=str, default="output/", help="Directory to write snapshots")
    p.add_argument("--log", type=str, default="INFO", help="Logging level")
    p.add_argument("--strategy", type=str, default="default",
                   help="Strategy to use in the simulation")
    p.add_argument("--past-attendenece", type=str,
                   default=[44, 78, 56, 15, 23, 67, 84, 34, 45, 76, 40, 56, 22, 35],
                   help="List with past attendence data")
    args = p.parse_args(argv)

    return args


def main(argv=None):
    cfg = parse_args(argv)

    start_time = timeit.default_timer()

    sim = Simulation(cfg)

    end_time = timeit.default_timer()
    print(f"Simulation took {end_time - start_time} seconds")

    print(cfg)
    print(sim)


if __name__ == "__main__":
    main()
