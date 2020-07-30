"""Main file
By Damon Jones for 11PRG 1.7 2020 Practice
"""
# Imports
import json
import os

from order import Order


# Functions
def load_ingredients(_dir : str) -> dict:
    ingredients = {}
    for filename in os.listdir(_dir):
        with open(os.path.join(_dir, filename), "r") as f:
            ingredients = {**ingredients, **json.load(f)}
    return ingredients


def load_restrictions(_dir : str) -> dict:
    restrictions = {}
    with open(os.path.join(_dir, "restrictions.json"), "r") as f:
        restrictions = json.load(f)
    return restrictions


# Main
def main() -> int:
    # Load Stuff
    ingredients = load_ingredients("Data/Ingredients")

    return 1


if __name__ == "__main__":
    status = main()

    print(f"Exited with status: {status}")