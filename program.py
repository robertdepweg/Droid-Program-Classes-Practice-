# Author: Robert Depweg
# Class: CIS226
# Date: 9/28/24
"""Program code"""
from user_interface import UserInterface
from droids import DroidCollection
import os

ui = UserInterface()
droid_collection = DroidCollection

def main(*args):
    """Method to run program"""
    ui.welcome_message()
    try:
        choice = ui.menu_choices()
    except:
        ui.value_error_message()

    while choice <= ui.MAX_MENU_CHOICES:
        if choice == 1:
            droid_info = ui.droid_info_prompt()
            droid_collection.add_to_collection(droid_info)
        if choice == 2:
            ui.print_collection()

        if choice == 3:
            os._exit

        choice = ui.menu_choices()