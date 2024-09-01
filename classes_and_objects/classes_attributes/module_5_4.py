from typing import Self


class House:
    houses_history = []

    def __new__(cls, *args) -> Self:
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")

    def __init__(self, name, number_of_floors) -> None:
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if self.number_of_floors < new_floor:
            print("Такого этажа не существует")
        else:
            for i in range(1, new_floor + 1):
                print(i)

    def _check_type(self, value):
        if not isinstance(value, type(self)):
            raise TypeError("Аргумент должен быть экземпляром House")

    def __len__(self):
        return self.number_of_floors

    def __str__(self) -> str:
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other) -> bool:
        self._check_type(other)
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other) -> bool:
        self._check_type(other)
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other) -> bool:
        self._check_type(other)
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other) -> bool:
        self._check_type(other)
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other) -> bool:
        self._check_type(other)
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other) -> bool:
        self._check_type(other)
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value: int) -> Self:
        if not isinstance(value, (int, float)):
            raise TypeError("Аргумент должен быть целым числом")
        self.number_of_floors += value
        return self

    def __radd__(self, value: int) -> Self:
        return self.__add__(value)

    def __iadd__(self, value: int) -> Self:
        return self.__add__(value)


h1 = House("ЖК Эльбрус", 10)
print(House.houses_history)
h2 = House("ЖК Акация", 20)
print(House.houses_history)
h3 = House("ЖК Матрёшки", 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
