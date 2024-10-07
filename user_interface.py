"""User interface module"""
# Author: Robert Depweg
# Class: CIS226
# Date: 9/28/24

class UserInterface:
    """"""

    MAX_MENU_CHOICES = 3

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
        """Prompts user for different characteristics of Droid, which is then be sent to DroidCollection"""
        info_tuple =+ input(f"What type of droid do you want? (Enter digit as input)--
                            1 - Protocol: $150 
                            2 - Utility: $100 
                            3 - Janitor: $50 
                            4 - Astromech: $200
                            > ") # Price for droid model
        info_tuple =+ input(f"What type of material do you want the droid to be made of?--
                            1 - Protocol: $150 
                            2 - Utility: $100 
                            3 - Janitor: $50 
                            4 - Astromech: $200
                            > ") # 4 different material choices, each w a diff price
        info_tuple =+ input(f"What should the color of the droid be?--
                            1 - Protocol: $150 
                            2 - Utility: $100 
                            3 - Janitor: $50 
                            4 - Astromech: $200
                            > ") # 4 diff color choices, w diff prices for each
        info_tuple =+ input(f"Type the digit for the droid you want--
                            1 - Protocol: $150 
                            2 - Utility: $100 
                            3 - Janitor: $50 
                            4 - Astromech: $200
                            > ") # a price for each additional option
        info_tuple =+ input(f"How many languages do you want the droid to have?--
                            1 - Protocol: $150 
                            2 - Utility: $100 
                            3 - Janitor: $50 
                            4 - Astromech: $200
                            > ") # a price per quantity option such as num of languages (10$ per option)
        return info_tuple

    def print_collection():
        """"""
        pass

    def choice_error():
        """"""
        pass