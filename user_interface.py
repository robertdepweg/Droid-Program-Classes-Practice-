"""User interface module"""
# Author: Robert Depweg
# Class: CIS226
# Date: 9/28/24

class UserInterface:
    """"""

    def welcome_message():
        """"""
        print("Welcome to the Droid Program.")


    def menu_choices():
        """Prints menu choices for user to pick"""
        print("1. Add a new Droid.")
        print("2. Print current Droid collection.")
        user_choice = input("> ", end="")
        return user_choice


    def droid_info_prompt():
        """Prompts user for different characteristics of Droid, which will then be sent to"""
        print() # Price for droid model
        print() # 4 different material choices, each w a diff price
        print() # 4 diff color choices, w diff prices for each
        print() # a price for each additional option
        print() # a price per quantity option such as num of languages (10$ per option)

        pass

    def print_collection():
        """"""
        pass