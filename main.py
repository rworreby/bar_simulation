#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse
import time
from bar_simulation import Simulation
from dataclasses import dataclass

"""
Bar Simulation main file.

Features:
-
"""

def parse_args(argv=None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Simulation boilerplate")
    p.add_argument("--duration", type=float, default=10.0, help="Simulated duration in weeks")
    p.add_argument("--output", type=str, default=None, help="Directory to write snapshots")
    p.add_argument("--log", type=str, default="INFO", help="Logging level")
    p.add_argument("--strategy", type=str, default="default", help="Strategy to use in the simulation")
    args = p.parse_args(argv)

    args.output_dir = args.output
    args.log_level = args.log

    return args


def main(argv=None):
    cfg = parse_args(argv)
    sim = Simulation(cfg)
    sim.initialize()
    sim.run()


if __name__ == "__main__":
    main()
