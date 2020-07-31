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


def get_bread(breads : list) -> str:
    """Gets user input for which bread they'd like.

    Args:
        breads (list): List of breads to choose from.

    Returns:
        str: The chosen bread.
    """
    print("What Bread Would you Like?\n")
    for i in range(len(breads)):
        print(f"{i + 1}\t: {breads[i]}")
    
    input_valid = False
    while not input_valid:
        bread_selection = input(f"\nEnter a Number Between 1 and {len(breads)}: ")
        try:
            bread_selection = int(bread_selection)
        except:
            continue
        input_valid = bread_selection >= 1 and bread_selection <= len(breads)
    
    return breads[bread_selection - 1]


def get_meat(meats : list) -> str:
    pass


def get_options(options : list) -> list:
    pass


# Main
def main() -> int:
    # Load Stuff
    ingredients = load_ingredients("Data/Ingredients")

    sandwich = Order()
    sandwich.bread = get_bread(ingredients["breads"])

    print(sandwich.bread)

    return 1


if __name__ == "__main__":
    status = main()

    print(f"Exited with status: {status}")