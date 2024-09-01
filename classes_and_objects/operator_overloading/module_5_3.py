from typing import Self


class House:
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

    def __eq__(self, other: Self) -> bool:
        self._check_type(other)
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other: Self) -> bool:
        self._check_type(other)
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other: Self) -> bool:
        self._check_type(other)
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other: Self) -> bool:
        self._check_type(other)
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other: Self) -> bool:
        self._check_type(other)
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other: Self) -> bool:
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
h2 = House("ЖК Акация", 20)

print(h1)
print(h2)

print(h1 == h2)  # __eq__

h1 = h1 + 10  # __add__
print(h1)
print(h1 == h2)

h1 += 10  # __iadd__
print(h1)

h2 = 10 + h2  # __radd__
print(h2)

print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__
