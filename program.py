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
