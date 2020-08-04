"""Main file
By Damon Jones for 11PRG 1.7 2020 Practice
"""
# Imports
import json
import os
import sys
import time

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


def get_username() -> str:
    """Gets the user's name.

    Returns:
        str: Desired username.
    """
    return input("Input username: ")


def get_bread(breads : list) -> str:
    """Gets user input for which bread they'd like.

    Args:
        breads (list): List of breads to choose from.

    Returns:
        str: The chosen bread.
    """
    print("\nWhat Bread Would you Like?\n")
    for i in range(len(breads)):
        print(f"{i + 1}\t: {breads[i]}")
    print("\n")
    
    input_valid = False
    while not input_valid:
        bread_selection = input(f"Enter a Number Between 1 and {len(breads)}: ")
        try:
            bread_selection = int(bread_selection)
        except:
            continue
        input_valid = bread_selection >= 1 and bread_selection <= len(breads)
    
    return breads[bread_selection - 1]


def get_meat(meats : list) -> str:
    """Gets user input for which meat they'd like.

    Args:
        meats (list): List of meats to choose from.

    Returns:
        str: The chosen meat.
    """
    
    # This function is effectively the same as get_bread except it works with meats instead.
    # I didn't really feel like making one function that can do both with fancy logic so I
    # just made two seperate functions for bread and meat.
    print("\nWhich Meat Would you Like?\n")
    for i in range(len(meats)):
        print(f"{i + 1}\t: {meats[i]}")
    print("\n")
    
    input_valid = False
    while not input_valid:
        meat_selection = input(f"Enter a Number Between 1 and {len(meats)}: ")
        try:
            meat_selection = int(meat_selection)
        except:
            continue
        input_valid = meat_selection >= 1 and meat_selection <= len(meats)
    
    return meats[meat_selection - 1]


def get_options(options : list) -> list:
    """Gets user input for what options they'd like.

    Args:
        options (list): List of options to choose from.

    Returns:
        list: The selected list of options for the order.
    """
    selections = [False] * len(options) #Initialize bool list - same size as the list of options

    # Selections list is a list of booleans representing whether an option from options 
    # is selected or not.

    print("Which Options Would you Like?\n")
    
    selecting = True
    while selecting:
        for i in range(len(options)):
            # I'm gonna break down this print statement so it's clear:
            # I'm printing the name of the option along with it's index + 1 int the list.
            # Before that I either print a space or a dash, depending on whether the option
            # is selected or not. This works as I can make a list contain ' ' and '-' and
            # index it using a boolean from the selections list, as False counts as 0 and
            # True counts as 1.
            print(f" {[' ', '-'][selections[i]]} {i + 1}\t: {options[i]}")
        
        print("\nEnter a number to toggle option")
        print("Enter nothing to continue\n")

        user_in = input(f"Enter a Number Between 1 and {len(options)}: ")
        print("\n\n\n\n")

        # Check whether input is a valid integer and if so do stuff with it.
        try:
            user_in = int(user_in) #Turn user input into integer
            if selections[user_in - 1]:
                selections[user_in - 1] = False
            elif check_number_of_selections(selections) < 4: #Make sure user doesn't have too many options.
                selections[user_in - 1] = True
        except:
            # Ends loop if user input is empty.
            if user_in == "":
                selecting = False
    
    selected_options = [] #Final list of options that have been selected
    # This loop just add an option to the final list of options if it's been selected.
    for i in range(len(options)):
        if selections[i]:
            selected_options.append(options[i])
    return selected_options


def check_number_of_selections(selections : list) -> int:
    """Checks number of options selected in a list.

    This is used to ensure that the user doesn't select more than four options, as
    the task suggests the program should.

    Args:
        selections (list): List of bools representing which options are selected.

    Returns:
        int: Number of options selected.
    """
    number_of_selections = 0
    for item in selections:
        if item:
            number_of_selections += 1
    return number_of_selections


def print_order(sandwich : Order) -> None:
    print("=======================")
    print("    YOUR ORDER IS    ")
    print("=======================")
    print(f"Bread:\t{sandwich.bread}")
    print(f"Meat:\t{sandwich.meat}")
    sys.stdout.write("Opts:") #Prints without a new line
    if len(sandwich.options) > 0:
        for item in sandwich.options:
            print(f"\t{item}")
    else:
        print("\t[none]")


# Main Function/Call
def main() -> int:
    while True:
        # Username Input
        username = ""
        try:
            username = get_username()
        except:
            return -3 #Username Input Error


        # Loading Ingredients
        try:
            ingredients = load_ingredients("Data/Ingredients")
        except:
            return -10 #File Loading Error


        # Sandwich Order (Putting it together)
        try:
            print(f"Hello {username}, please enter your order...")
            sandwich = Order()
            time.sleep(1)

            sandwich.bread = get_bread(ingredients["breads"])
            print(f"You picked: {sandwich.bread}")
            time.sleep(1)
            print("\n\n=======================\n\n")

            sandwich.meat = get_meat(ingredients["meats"])
            print(f"You picked: {sandwich.meat}")
            time.sleep(1)
            print("\n\n=======================\n\n")

            sandwich.options = get_options(ingredients["options"])
            print(f"You picked: {', '.join(sandwich.options)}")
            time.sleep(1)
        except:
            return -1 #Sandwich Order Error


        # Printing out Sandwich Order
        try:
            print_order(sandwich)
            print("\n\n\n\n")
            input("Press enter to continue...")
            print("\n\n\n\n")
        except:
            return -2 #Sandwich Print Error

    return 1


if __name__ == "__main__":
    status = main()

    print(f"Exited with status: {status}") #For debug purposes
    # Exit Statuses:
    #   1 : OK
    #  -1 : Sandwich Order Error
    #  -2 : Sandwich Print Error
    #  -3 : Username Input Error
    # -10 : File Loading Error