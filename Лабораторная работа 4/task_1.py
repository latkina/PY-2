class Transport:
    """
    Документация для класса
    Класс описывает модель транспортного средства
    """
    def __init__(self, name: str, speed: (int, float)):
        """
        Создание и подготовка к эксплуатации объекта "Транспорт"

        :param name: Название транспортного средства
        :param speed: Скорость транспортного средства (км/ч)

        Example:
        >>> transport = Transport("поезд", 60)
        """
        self._name = name
        self._speed = speed

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def pages(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError
        self._name = name

    @property
    def speed(self) -> (int, float):
        return self._speed

    @speed.setter
    def speed(self, speed: (int, float)) -> None:
        if not isinstance(speed, (int, float)):
            raise TypeError
        if not speed > 0:
            raise ValueError
        self._speed = speed

    def __str__(self):
        return f"Транспорт: {self.name}. Скорость передвижения: {self.speed}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, speed={self.speed!r})"


class GroundTransport(Transport):
    """
    Документация для класса
    Класс описывает модель наземного транспортного средства
    """
    def __init__(self, name: str, speed: (int, float), vehicle_category: str):
        """
        Создание и подготовка к эксплуатации объекта "Наземный транспорт"

        :param name: Название транспортного средства
        :param speed: Скорость транспортного средства (км/ч)
        :param vehicle_category: Категория транспортного средства (как в водительских правах)

        Example:
        >>> ground_transport = GroundTransport("автомобиль", 180, "B")
        """
        super().__init__(name, speed)
        self._vehicle_category = vehicle_category

    @property
    def vehicle_category(self) -> str:
        return self._vehicle_category

    @vehicle_category.setter
    def vehicle_category(self, vehicle_category: str) -> None:
        if not isinstance(vehicle_category, str):
            raise TypeError
        self._vehicle_category = vehicle_category

    def __str__(self):
        return f"Транспорт: {self.name}. Скорость передвижения: {self.speed}. Категория транспортного средства: {self.vehicle_category}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, speed={self.speed!r}, vehicle_category={self.vehicle_category!r})"


class AirTransport(Transport):
    """
    Документация для класса
    Класс описывает модель воздушного транспортного средства
    """
    def __init__(self, name: str, speed: (int, float), flight: str):
        """
        Создание и подготовка к эксплуатации объекта "Воздушный транспорт"

        :param name: Название транспортного средства
        :param speed: Скорость транспортного средства (км/ч)
        :param flight: Вид рейсов, совершаемых этим транспортом (внутренние/международные)

        Example:
        >>> air_transport = AirTransport("Боинг 737", 745, "внутренние рейсы")
        """
        super().__init__(name, speed)
        self._flight = flight

    @property
    def flight(self) -> float:
        return self._flight

    @flight.setter
    def flight(self, flight: str) -> None:
        if not isinstance(flight, str):
            raise TypeError
        self._flight = flight

    def __str__(self):
        return f"Транспорт: {self.name}. Скорость передвижения: {self.speed}. Тип перелётов: {self.flight}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, speed={self.speed!r}, flight={self.flight!r})"


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    pass
