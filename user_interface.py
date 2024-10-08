"""User interface module"""
# Author: Robert Depweg
# Class: CIS226
# Date: 9/28/24

class UserInterface:
    """"""

    MAX_MENU_CHOICES = 3

    def welcome_message(self):
        """"""
        print("Welcome to the Droid Program.")


    def menu_choices(self):
        """Prints menu choices for user to pick"""
        try:
            print("1. Add a new Droid.")
            print("2. Print current Droid collection.")
            user_choice = input("> ", end="")
            return user_choice
        except ValueError:
            raise ValueError
        except Exception as message:
            print(message)

    def droid_info_prompt(self):
        """Prompts user for different characteristics of Droid, which is then be sent to DroidCollection"""
        info_tuple =+ input(f"What type of droid do you want? (Enter digit as input)--"
                            f"1 - Protocol: $150"
                            f"2 - Utility: $100"
                            f"3 - Janitor: $50" 
                            f"4 - Astromech: $200"
                            f"> ") # Price for droid model
        info_tuple =+ input(f"What type of material do you want the droid to be made of?--"
                            f"1 - Aluminum: $150" 
                            f"2 - Iron: $100"
                            f"3 - Copper: $50"
                            f"4 - Love: $200"
                            f"> ") # 4 different material choices, each w a diff price
        info_tuple =+ input(f"What should the color of the droid be?--"
                            f"1 - Gold: $150"
                            f"2 - Silver: $100"
                            f"3 - Bronze: $50"
                            f"4 - Periwinkle: $200"
                            f"> ") # 4 diff color choices, w diff prices for each
        info_tuple =+ input(f"Type the digit for the droid you want--"
                            f"1 - Protocol: $150"
                            f"2 - Utility: $100"
                            f"3 - Janitor: $50"
                            f"4 - Astromech: $200"
                            f"> ") # a price for each additional option
        info_tuple =+ input(f"How many languages do you want the droid to have?--"
                            f"1 - $150" 
                            f"2 - $100" 
                            f"3 - $50" 
                            f"4 - $200"
                            f"> ") # a price per quantity option such as num of languages (10$ per option)
        return info_tuple

    def print_collection(self):
        """"""
        pass

    def value_error_message(self):
        """"""
        print("That's an invalid input. Please try again.")
        pass