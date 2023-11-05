import setuptools
import os

from coconut.api import cmd


if __name__ == "__main__":
    cmd([os.path.join(os.path.dirname(__file__), "pathfinder_character_sheet")])

setuptools.setup(
    name="pathfinder_character_sheet",
    version="0.0.1",
    packages=setuptools.find_packages(),
)
