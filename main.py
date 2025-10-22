#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Bar Simulation main file.

Features:
-
"""

import argparse
import timeit
import bar_simulation.simulation as simulation


def parse_args(argv=None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Simulation setup parameters")
    p.add_argument("--duration", type=int, default=100, help="Simulated duration in weeks")
    p.add_argument("--output_dir", type=str, default="output/", help="Directory to write snapshots")
    p.add_argument("--log", type=str, default="INFO", help="Logging level")
    p.add_argument("--strategy", type=str, default="arthur",
                   help="Strategy to use in the simulation")
    p.add_argument("--past-attendenece", type=str,
                   default=[44, 78, 56, 15, 23, 67, 84, 34, 45, 76, 40, 56, 22, 35],
                   help="List with past attendence data")
    args = p.parse_args(argv)

    return args


def main(argv=None):
    cfg = parse_args(argv)

    start_time = timeit.default_timer()
    sim = simulation.Simulation(cfg)
    sim.initialize()
    end_time = timeit.default_timer()
    print(f"Simulation setup completed in {round(end_time - start_time, 4)} seconds.")
    print(f"Simulation Parameters: {sim}\n")

    print("Starting simulation.\n")
    start_time = timeit.default_timer()
    sim.run()
    end_time = timeit.default_timer()
    print(f"Simulation execution completed in {round(end_time - start_time, 4)} seconds.")

    print(f"Saving simulation results to {cfg.output_dir} and plotting data.")
    start_time = timeit.default_timer()
    sim.save_data()
    sim.plot_data()
    end_time = timeit.default_timer()
    print(f"Data saving and plotting completed in {round(end_time - start_time, 4)} seconds.")


if __name__ == "__main__":
    main()
