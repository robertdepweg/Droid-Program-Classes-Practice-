"""Droid module"""

# Author: Robert Depweg
# Class: CIS226
# Date: 9/28/24

from abstract_droid import AbstractDroid


class Droid(AbstractDroid):
    """Abstract base class derived from AbstractDroid"""

    def __init__(self, material, color):
        """Constructor"""
        self.material = material
        self.color = color
        super().__init__()

    def __str__(self):
        """Returns a formatted string containing the variables"""
        return f"Material: {self.material} Color: {self.color}"

    def calculate_total_cost(self):
        """"""
        total_cost = 0.0
        super().calculate_total_cost(total_cost)


class Protocol(Droid):
    """Class derived from Droid"""

    COST_PER_LANGUAGE = 10.00

    def __init__(self, material, color, number_of_languages):
        """"""
        super().__init__(material, color)
        self.number_of_languages = number_of_languages

    def calculate_total_cost(self):
        """"""
        return super().calculate_total_cost(self.number_of_languages * self.COST_PER_LANGUAGE)


class Utility(Droid):
    """Class derived from Droid, parent class to Janitor and Astromech"""

    def __init__(self, material, color, toolbox, computer_connection, scanner):
        """"""
        super().__init__(material, color)
        self.toolbox = toolbox
        self.computer_connection = computer_connection
        self.scanner = scanner

    def __str__():
        """"""
        pass

    def calculate_total_cost(self) -> None:
        """"""
        pass


class Janitor(Utility):
    """Class derived from Utility"""

    def __init__(self, material, color, toolbox, computer_connection, scanner, broom, vacuum):
        """"""
        super().__init__(material, color, toolbox, computer_connection, scanner)
        self.broom = broom
        self.vacuum = vacuum

    def __str__():
        """"""
        pass

    def calculate_total_cost(self) -> None:
        """"""
        return super().calculate_total_cost()


class Astromech(Utility):
    """Class derived from Utility"""

    COST_PER_SHIP = 40.00

    def __init__(self, material, color, toolbox, computer_connection, scanner, navigation, number_of_ships):
        """"""
        super().__init__(material, color, toolbox, computer_connection, scanner)
        self.navigation = navigation
        self.number_of_ships = number_of_ships

    def __str__(toolbox, computer_connection, scanner, navigation, number_of_ships):
        """"""
        navigation = "True" if self.navigation else "False"
        number_of_ships = "True" if self.number_of_ships else "False"
        return f"{super().__str__()}{toolbox}{computer_connection}{scanner}{navigation}{number_of_ships}"

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
        return_string = ""
        for droid in DroidCollection:
            return_string.append(droid)
        print(return_string)

    def _add_protocol(self, droid_info):
        """Uses Droid __str__ constructor to format string"""
        self.__droid_collection.append(Protocol(droid_info[1:]))

    def _add_utility(self, droid_info):
        """Uses Droid __str__ constructor to format string"""
        self.__droid_collection.append(Utility(droid_info[1:]))

    def _add_janitor(self, droid_info):
        """Uses Droid __str__ constructor to format string"""
        self.__droid_collection.append(Janitor(droid_info[1:]))

    def _add_astromech(self, droid_info):
        """Uses Droid __str__ constructor to format string"""
        self.__droid_collection.append(Astromech(droid_info[1:]))

    def total_cost():
        """"""
        pass
