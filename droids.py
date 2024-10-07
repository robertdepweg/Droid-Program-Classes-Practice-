# Author: Robert Depweg
# Class: CIS226
# Date: 9/28/24
"""Droid module"""

from abstract_droid import AbstractDroid


class Droid(AbstractDroid):
    """Abstract base class derived from AbstractDroid"""
    
    material = ''
    color = ''
    total_cost = 0.0

    def __init__(self, material, color):
        """Constructor"""
        super().__init__(material, color)

    def __str__(self):
        """Returns a formatted string containing the variables"""
        pass

    def calculate_total_cost(self):
        """"""
        return super().calculate_total_cost()


class Protocol(Droid):
    """Class derived from Droid"""

    COST_PER_LANGUAGE = 10.00

    number_of_languages = 0

    def __init__(self, material, color, number_of_languages):
        """"""
        super().__init__(material, color)


    def calculate_total_cost(self) -> None:
        """"""
        return super().calculate_total_cost()


class Utility(Droid):
    """Class derived from Droid, base class to Janitor and Astromech"""

    toolbox = False
    computer_connection = False
    scanner = False

    def __init__(self, material, color, toolbox, computer_connection, scanner):
        """"""
        super().__init__(material, color)

    def calculate_total_cost(self) -> None:
        """"""
        pass


class Janitor(Utility):
    """Class derived from Utility"""

    broom = False
    vacuum = False

    def __init__(self, material, color, toolbox, computer_connection, scanner, broom, vacuum):
        """"""
        super().__init__()

    def calculate_total_cost(self) -> None:
        """"""
        return super().calculate_total_cost()


class Astromech(Utility):
    """Class derived from Utility"""
    
    COST_PER_SHIP = 40.00

    navigation = False
    number_of_ships = False

    def __init__(self, material, color, toolbox, computer_connection, navigation, number_of_ships, INT):
        """"""
        super().__init__()



    def calculate_total_cost(self) -> None:
        """"""
        return super().calculate_total_cost()
    
class DroidCollection:
    """"""
    def __init__(self):
        """"""
        self.__droid_collection = []

    def __str__():
        """"""
        for droid in DroidCollection:
            print(droid)
        pass

    def add_to_collection():
        """"""
        pass

    def total_cost():
        """"""
        pass