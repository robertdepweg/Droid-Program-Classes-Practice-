"""Droid module"""

# Author: Robert Depweg
# Class: CIS226
# Date: 9/28/24

from abstract_droid import AbstractDroid


class Droid(AbstractDroid):
    """Abstract base class derived from AbstractDroid"""

    def __init__(self, material, color):
        """Constructor"""
        self._material = material
        self._color = color
        super().__init__()

    def __str__(self):
        """Returns a formatted string containing the variables"""
        return f"Material: {self.material} | Color: {self.color} | Total Cost: {self.calculate_total_cost}"
    
    @property
    def material(self):
        """Property for material"""
        return self._material
    
    @property
    def color(self):
        """Property for color"""
        return self._color

    @property
    def calculate_total_cost(self):
        """Calculates total cost of droid"""
        total_cost = 0.0
        super().calculate_total_cost(total_cost)

    # def format_decimal?


class Protocol(Droid):
    """Class derived from Droid"""

    COST_PER_LANGUAGE = 10.00

    def __init__(self, material, color, number_of_languages):
        """Constructor"""
        super().__init__(material, color)
        self._number_of_languages = number_of_languages

    def __str__(self):
        """Returns a formatted string containing the variables"""
        return f"{super.__str__()}| Number of languages: {self.number_of_languages}"

    @property
    def number_of_languages(self):
        """Property for number of langauges"""
        return self._number_of_languages
    
    def calculate_total_cost(self):
        """Calculates total cost of droid"""
        return super().calculate_total_cost(self.number_of_languages * self.COST_PER_LANGUAGE)


class Utility(Droid):
    """Class derived from Droid, parent class to Janitor and Astromech"""

    def __init__(self, material, color, toolbox, computer_connection, scanner):
        """Constructor"""
        super().__init__(material, color)
        self._toolbox = toolbox
        self._computer_connection = computer_connection
        self._scanner = scanner

    def __str__(self):
        """Returns a formatted string containing the variables"""
        return f"{super.__str__()}{self.toolbox}{self.computer_connection}{self.scanner}"
    
    @property
    def toolbox(self):
        """Property for toolbox"""
        return self._toolbox
    
    @property
    def computer_connection(self):
        """Property for computer_connection"""
        return self._computer_connection
    
    @property
    def scanner(self):
        """Property for scanner"""
        return self._scanner
    
    def calculate_total_cost(self) -> None:
        """Calculates total cost of droid"""
        pass


class Janitor(Utility):
    """Class derived from Utility"""

    def __init__(self, material, color, toolbox, computer_connection, scanner, broom, vacuum):
        """Constructor"""
        super().__init__(material, color, toolbox, computer_connection, scanner)
        self._broom = broom
        self._vacuum = vacuum

    def __str__(self):
        """Returns a formatted string containing the variables"""
        return f"{super.__str__()}{self.broom}{self.vacuum}"
    
    @property
    def broom(self):
        """Property for broom"""
        return self._broom
    
    @property
    def vacuum(self):
        """Property for vacuum"""
        return self._vacuum
    
    def calculate_total_cost(self) -> None:
        """Calculates total cost of droid"""
        return super().calculate_total_cost()


class Astromech(Utility):
    """Class derived from Utility"""

    COST_PER_SHIP = 40.00

    def __init__(self, material, color, toolbox, computer_connection, scanner, navigation, number_of_ships):
        """Constructor"""
        super().__init__(material, color, toolbox, computer_connection, scanner)
        self._navigation = navigation
        self._number_of_ships = number_of_ships

    def __str__(self):
        """Returns a formatted string containing the variables"""
        # navigation = "True" if self.navigation else "False"
        # number_of_ships = "True" if self.number_of_ships else "False"
        return f"{super().__str__()}{self.navigation}{self.number_of_ships}"
    
    @property
    def navigation(self):
        """Property for navigation"""
        return self._navigation

    @property
    def number_of_ships(self):
        """Property for number of ships"""
        return self._number_of_ships
    
    def calculate_total_cost(self) -> None:
        """Calculates total cost of droid"""
        return super().calculate_total_cost()


class DroidCollection:
    """Droid collection class"""

    def __init__(self):
        """Constructor"""
        self.__droid_collection = []

    def __str__(self):
        """Returns a formatted string containing each droid"""
        for droid in DroidCollection:
            print(droid)

    def _add_protocol(self, droid_info):
        """Uses Droid __str__ constructor to format string"""
        self.__droid_collection.append(Protocol(droid_info[1],droid_info[1],droid_info[1],droid_info[1]))

    def _add_utility(self, droid_info):
        """Uses Droid __str__ constructor to format string"""
        self.__droid_collection.append(Utility(droid_info[1],droid_info[1],droid_info[1],droid_info[1],droid_info[1]))

    def _add_janitor(self, droid_info):
        """Uses Droid __str__ constructor to format string"""
        self.__droid_collection.append(Janitor(droid_info[1],droid_info[1],droid_info[1],droid_info[1],droid_info[1],droid_info[1],droid_info[1],))

    def _add_astromech(self, droid_info):
        """Uses Droid __str__ constructor to format string"""
        self.__droid_collection.append(Astromech(droid_info[1],droid_info[1],droid_info[1],droid_info[1],droid_info[1],droid_info[1],droid_info[1],))
