# Author: Robert Depweg
# Class: CIS226
# Date: 9/28/24
"""Program code"""
from user_interface import UserInterface

ui = UserInterface()

def main(*args):
    """Method to run program"""
    ui.welcome_message()

    choice = ui.menu_choices()

    while choice != ui.MAX_MENU_CHOICES:
        if choice == 1:
            ui.droid_info_prompt()

        if choice == 2:

        else:
