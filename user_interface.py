"""User interface module"""
# Author: Robert Depweg
# Class: CIS226
# Date: 9/28/24

class UserInterface:
    """"""

    MAX_MENU_CHOICES = 3

    def welcome_message(self):
        """"""
        print("\nWelcome to the Droid Program.")


    def menu_choices(self):
        """Prints menu choices for user to pick"""
        try:
            print("\n1. Add a new Droid.")
            print("\n2. Print current Droid collection.")
            print("\n> ", end="")
            user_choice = int(input())
            return user_choice
        except ValueError:
            raise ValueError
        except Exception as message:
            print(message)

    def droid_info_prompt(self):
        """Prompts user for different characteristics of Droid, which is then be sent to DroidCollection"""
        user_info_list = []
        droid_info_list = [[Protocol, Utility, ][][][][]]

        user_info_list.append(input(f"What type of droid do you want? (Enter digit as input)--\n"
                            f"1 - Protocol: $150\n"
                            f"2 - Utility: $100\n"
                            f"3 - Janitor: $50\n" 
                            f"4 - Astromech: $200\n"
                            f"> ")) # Price for droid model
        user_info_list.append(f"What type of material do you want the droid to be made of?--\n"
                            f"1 - Aluminum: $150\n" 
                            f"2 - Iron: $100\n"
                            f"3 - Copper: $50\n"
                            f"4 - Love: $200\n"
                            f"> ") # 4 different material choices, each w a diff price
        user_info_list.append(f"What should the color of the droid be?--\n"
                            f"1 - Gold: $150\n"
                            f"2 - Silver: $100\n"
                            f"3 - Bronze: $50\n"
                            f"4 - Periwinkle: $200\n"
                            f"> ") # 4 diff color choices, w diff prices for each
        user_info_list.append(f"Type the digit for the droid you want--"
                            f"1 - Protocol: $150\n"
                            f"2 - Utility: $100\n"
                            f"3 - Janitor: $50\n"
                            f"4 - Astromech: $200\n"
                            f"> ") # a price for each additional option
        user_info_list.append(f"How many languages do you want the droid to have?--"
                            f"1 - $150\n" 
                            f"2 - $100\n" 
                            f"3 - $50\n" 
                            f"4 - $200\n"
                            f"> ") # a price per quantity option such as num of languages (10$ per option)
        return user_info_list

    def print_collection(self):
        """"""
        pass

    def value_error_message(self):
        """"""
        print("\nThat's an invalid input. Please try again.")
        pass