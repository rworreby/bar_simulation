import os
import sys

PROJECT_PATH = os.getcwd()
SOURCE_PATH = os.path.join(
    PROJECT_PATH, "bar_simulation"
)
sys.path.append(SOURCE_PATH)