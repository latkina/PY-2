import doctest


class Animals:
    """
    Documentation for the class
    The class describes the animal model
    """
    def __init__(self, name: str, class_: str, weight: (int, float)):
        """
        Creation and preparation for operation of the "Animals" object

        :param name: Name of animals
        :param class_: Animal class
        :param weight: Animal weight

        Example:
        >>> animal = Animals("cat", "mammal", 3.5)
        """
        if not isinstance(name, str):
            raise TypeError("Invalid variable type, enter the word")
        self.name_of_animals = name

        if not isinstance(class_, str):
            raise TypeError("Invalid variable type, enter the word")
        self.animal_class = class_

        if not isinstance(weight, (int, float)):
            raise TypeError("Invalid variable type, enter a number")
        if weight <= 0:
            raise ValueError("The weight of the animal must be a positive number")
        self.animal_weight = weight

    def is_pet(self) -> bool:
        """
        A function that checks whether a pet is

        :return: Is it a pet?
        """
        ...

    def is_big(self) -> bool:
        """
        A function that checks if the animal is big

        :return: Is the animal big?
        """
        ...


class Socks:
    """
    Documentation for the class
    The class describes the model of socks
    """
    def __init__(self, colour: str, size: (int, float)):
        """
        Creation and preparation for operation of the "Socks" object

        :param colour: Socks colour
        :param size: Sock size

        Example:
        >>> socks = Socks("black", 6)
        """
        if not isinstance(colour, str):
            raise TypeError("Invalid variable type, enter the word")
        self.socks_colour = colour

        if not isinstance(size, (int, float)):
            raise TypeError("Invalid variable type, enter a number")
        if size <= 0:
            raise ValueError("The size of the socks must be a positive number")
        self.sock_size = size

    def sock_sizing_grid(self) -> str:
        """
        A function that checks in which size grid the size of socks is specified (EU or USA)

        :return: What size grid do socks belong to ("EU" or "US")?
        """
        ...

    def is_black(self) -> bool:
        """
        A function that checks if a sock is black

        :return: Is the sock black?
        """
        ...


class Chocolate:
    """
    Documentation for the class
    The class describes the chocolate model
    """
    def __init__(self, length: (int, float), width: (int, float)):
        """
        Creation and preparation for operation of the "Chocolate" facility

        :param length: Сhocolate bar length
        :param width: Сhocolate bar width

        Example:
        >>> chocolate = Chocolate(17.5, 7)
        """
        self.chocolate_filling = []

        if not isinstance(length, (int, float)):
            raise TypeError("Invalid variable type, enter a number")
        if length <= 0:
            raise ValueError("The length of the chocolate bar must be a positive number")
        self.chocolate_length = length

        if not isinstance(width, (int, float)):
            raise TypeError("Invalid variable type, enter a number")
        if not width > 0:
            raise ValueError("The width of the chocolate bar must be a positive number")
        self.chocolate_width = width

    def add_filling(self, filling: str) -> None:
        """
        A function that adds a filling to the chocolate

        :param filling: Filling in chocolate
        """
        ...

    def calc_area(self) -> str:
        """
        The function that determines the size of the chocolate bar ("S", "M" or "L")

        :return: What is the size of a chocolate bar ("S", "M" or "L")?
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
