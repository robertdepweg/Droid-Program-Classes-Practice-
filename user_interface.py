"""User interface module"""

# Author: Robert Depweg
# Class: CIS226
# Date: 9/28/24

class UserInterface:
    """"""

    MAX_MENU_CHOICES = 2

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
            if user_choice > self.MAX_MENU_CHOICES:
                raise IndexError
            return user_choice
        except ValueError:
            raise ValueError

    def droid_option_prompt(self):
        """Prompts user for different characteristics of Droid, before going into specific pathways"""
        # Stores numbers to be sent to DroidCollection
        droid_info = []

        try:
             # Price for droid model
            droid_info.append(
                input(
                    f"\nWhat type of droid do you want? (Enter digit as input)--\n"
                    f"1 - Protocol: $150\n"
                    f"2 - Utility: $100\n"
                    f"3 - Janitor: $50\n"
                    f"4 - Astromech: $200\n"
                    f"\n> "
                )
            )

            # Asks for material of droid
            droid_info.append(
                input(
                    f"\nWhat type of material do you want the droid to be made of?--\n"
                    f"5 - Aluminum: $150\n"
                    f"6 - Iron: $100\n"
                    f"7 - Copper: $50\n"
                    f"8 - Love: $200\n"
                    f"\n> "
                )
            )  
            
            # Asks for color of droid
            droid_info.append(
                input(
                    f"\nWhat should the color of the droid be?--\n"
                    f"9 - Gold: $150\n"
                    f"10 - Silver: $100\n"
                    f"11 - Bronze: $50\n"
                    f"12 - Periwinkle: $200\n"
                    f"\n> "
                )   
            )  
        
        except ValueError:
            raise ValueError
        
        return droid_info

    def protocol_options(self, droid_info):
        """Asks for number of languages"""
        try:
            # Asks for number of languages
            droid_info.append(
                    input(f"\nHow many languages do you want the droid to have?--\n"
                    f"\n> "
                )
            )  
            return droid_info
        except ValueError: 
            raise ValueError
        
                
    def utility_options(self, droid_info):
        """Asks for toolbox, computer_connection, and scanner availability"""
        try:
            # Asks for number of languages
            droid_info.append(
                input(
                    f"Do you want a toolbox included?--\n"
                    f"Yes: $150\n"
                    f"No: $100\n"
                )
            )  

            # Asks for number of languages
            droid_info.append(
                input(
                    f"Do you want the droid to be connecteted to a computer?--\n"
                    f"Yes: $150\n"
                    f"No: $100\n"
                )
            )  

            droid_info.append(
                input(
                    f"Do you want a scanner built into the droid?--\n"
                    f"Yes: $150\n"
                    f"No: $100\n"
                )
            )  
            
            return droid_info
        except ValueError: 
            raise ValueError

    def janitor_options(self, droid_info):
        """Asks for broom and vacuum availability"""
        try:
            droid_info.append(int(
                input(
                    f"Do you want the droid to come with a broom?--\n"
                    f"Yes: "
                    f"No: "
                    f"> "
                ))
            )  

            droid_info.append(
                input(
                    f"Do you want the droid to come with a vacuum?--\n"
                    f"Yes: "
                    f"No: "
                    f"> "
                )
            )  
            
            return droid_info
        except ValueError: 
            raise ValueError

    def astromech_options(self, droid_info):
        """Asks for navigational ability"""
        try:
            droid_info.append(
                input(
                    f"Do you want the droid to come with navigation tools?--\n"
                    f"Yes: "
                    f"No: "
                    f"> "
                )
            )  

            return droid_info
        except ValueError: 
            raise ValueError
        
    def true_or_false_check(self, value):
        """"""
        if value == 'Yes':
            True
        elif value == 'No':
            False

    def print_collection(self):
        """"""
        print("\nPrinting collection...")

    def value_error_message(self):
        """Prints value error message"""
        print(f"\nThat's an invalid input. Please try again.")

    def print_out_of_range_error(self):
        """Prints error if digit is greater than 2"""
        print(f"\nPlease type a digit less than three.")
