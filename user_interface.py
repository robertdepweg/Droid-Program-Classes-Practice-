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
            print("\n1. Add a new Droid.")
            print("2. Print current Droid collection.")
            print("\n> ", end="")
            user_choice = int(input())
            return user_choice
        except ValueError:
            raise ValueError
        except Exception as message:
            print(message)

    def droid_option_prompt(self):
        """Prompts user for different characteristics of Droid, which is then be sent to DroidCollection"""
        # Stores numbers to be sent to DroidCollection
        user_droid_options = []

        try:
             # Price for droid model
            user_droid_options.append(
                input(
                    f"\nWhat type of droid do you want? (Enter digit as input)--\n"
                    f"1 - Protocol: $150\n"
                    f"2 - Utility: $100\n"
                    f"3 - Janitor: $50\n"
                    f"4 - Astromech: $200\n"
                    f"> "
                )
            )

            # 4 different material choices, each w a diff price
            user_droid_options.append(
                input(
                    f"\nWhat type of material do you want the droid to be made of?--\n"
                    f"5 - Aluminum: $150\n"
                    f"6 - Iron: $100\n"
                    f"7 - Copper: $50\n"
                    f"8 - Love: $200\n"
                    f"> "
                )
            )  
            
            # 4 diff color choices, w diff prices for each
            user_droid_options.append(
                input(
                    f"\nWhat should the color of the droid be?--\n"
                    f"9 - Gold: $150\n"
                    f"10 - Silver: $100\n"
                    f"11 - Bronze: $50\n"
                    f"12 - Periwinkle: $200\n"
                    f"> "
                )   
            )  
        
        except ValueError:
            raise ValueError
        
        return user_droid_options

    def protocol_options(droid_info):
        """Asks for number of languages"""
        # Asks for number of languages, the more languages the more expensive
        droid_info.append(
                input(f"\nHow many languages do you want the droid to have?--\n"
                f"1 - $150\n"
                f"2 - $100\n"
                f"3 - $50\n"
                f"4 - $200\n"
                f"> "
            )
        )  
        return droid_info
                
    def utility_options(droid_info):
        """Asks for toolbox, computer_connection, and scanner availability"""
        droid_info.append(
            input(
                f"What type of droid do you want?--\n"
                f"13 - Protocol: $150\n"
                f"14 - Utility: $100\n"
                f"15 - Janitor: $50\n"
                f"16 - Astromech: $200\n"
                f"> "
            )
        )  
        
        return droid_info

    def janitor_options(droid_info):
        """Asks for broom and vacuum availability"""
        # Janitor pathway
        # a price for each additional option
        droid_info.append(
            input(
                f"Do you want the droid to come with a broom?--\n"
                f"13 - Protocol: $150\n"
                f"14 - Utility: $100\n"
                f"15 - Janitor: $50\n"
                f"16 - Astromech: $200\n"
                f"> "
            )
        )  

        droid_info.append(
            input(
                f"Do you want the droid to come with a vacuum?--\n"
                f"13 - Protocol: $150\n"
                f"14 - Utility: $100\n"
                f"15 - Janitor: $50\n"
                f"16 - Astromech: $200\n"
                f"> "
            )
        )  
        
        return droid_info

    def astromech_options(droid_info):
        """Asks for navigational ability"""
        # a price for each additional option
        droid_info.append(
            input(
                f"Do you want the droid to come with navigation tools?--\n"
                f"13 - Protocol: $150\n"
                f"14 - Utility: $100\n"
                f"15 - Janitor: $50\n"
                f"16 - Astromech: $200\n"
                f"> "
            )
        )  

        return droid_info

    def print_collection(self):
        """"""
        print("\nPrinting collection...")

    def value_error_message(self):
        """Prints value error message"""
        print("\nThat's an invalid input. Please try again.")
