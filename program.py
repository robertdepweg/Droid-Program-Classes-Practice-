"""Program code"""

# Author: Robert Depweg
# Class: CIS226
# Date: 9/28/24

# System Imports
from user_interface import UserInterface
import droids
import os

ui = UserInterface()
droid_collection = droids.DroidCollection()


def main(*args):
    """Method to run program"""
    ui.welcome_message()
    try:
        choice = ui.menu_choices()
    except:
        ui.value_error_message()

    while choice <= ui.MAX_MENU_CHOICES:
        if choice == 1:
            # Adds a droid
            droid_info = ui.droid_option_prompt()

            # The protocol droid path
            if droid_info == '1':
                ui.protocol_options(droid_info)
                droids.DroidCollection._add_protocol(droid_info)

            # The utility droid path
            elif droid_info == '2':
                ui.utility_options(droid_info)
                droids.DroidCollection._add_utility(droid_info)

            # The janitor droid path
            elif droid_info[0] == '3':
                ui.janitor_options(droid_info)
                droids.DroidCollection._add_janitor(droid_info)

            # The astromech droid path
            elif droid_info[0] == '4':
                ui.astromech_options(droid_info)
                droids.DroidCollection._add_astromech(droid_info)

        elif choice == 2:
            # Printing collection path
            ui.print_collection()
            print(droids.DroidCollection)
        elif choice == 3:
            # Exits program
            os._exit

        choice = ui.menu_choices()
