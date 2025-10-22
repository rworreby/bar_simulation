#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
print(sys.version)

from bar_simulation.person import Person
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style("darkgrid")
print("Imported seaborn and matplotlib for plotting.")


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
        self.population = []
        self.attendence = []

    def __str__(self) -> str:
        return f"Simulation Parameters: \n\
            Simulation duration: {self.duration}, \n\
            Output dir: {self.output_dir}, \n\
            Strategy: {self.strategy}, \n\
            Past attendence: {self.past_attendence}"

    @classmethod
    def get_num_weeks(self):
        """Returns number of weeks the simulation runs for."""
        return self.duration

    def initialize(self):
        """Initializes the simulation."""
        for i in range(100):
            self.population.append(Person(strategy=self.strategy))
        print(f"Initialized population with {len(self.population)} persons and "
              f"strategy {self.strategy}.")

    def run(self):
        """Runs the simulation."""
        for week in range(self.duration):
            for person in self.population:
                decision = person.strategy.make_decision()
                person.attendence.append(decision)
            week_attendence = sum([p.attendence[-1] for p in self.population])
            self.attendence.append(week_attendence)
            print(f"Week {week + 1}: Attendence = {week_attendence}")

    def save_data(self):
        """Saves the simulation data to output directory."""
        with open(f"{self.output_dir}/attendence.csv", "w") as f:
            f.write('week,attendence\n')
            for week, attendence in enumerate(self.attendence):
                f.write(f"{week + 1},{attendence}\n")
        print(f"Saved attendence data to {self.output_dir}/attendence.csv")

    def plot_data(self):
        """Plots the simulation data."""
        weeks = list(range(1, self.duration + 1))
        plt.plot(weeks, self.attendence)
        plt.xlabel('Week')
        plt.ylabel('Attendence')
        plt.title('Bar Attendence Over Time With ' + self.strategy.capitalize() + ' Strategy')
        plt.savefig(f"{self.output_dir}/attendence_plot.pdf")
        plt.close()
        print(f"Saved attendence plot to {self.output_dir}/attendence_plot.pdf")