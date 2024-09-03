import math


class Figure:
    sides_count = 0

    def __init__(self, color, *sides, filled=True) -> None:
        self._init_sides(self.sides_count, *sides)
        self.set_color(*color)
        self.filled = filled

    def _init_sides(self, sides_count, *sides):
        if len(sides) == sides_count:
            self.set_sides(*sides)
        else:
            self.__sides = (1,) * sides_count

    def __len__(self):
        return sum(self.__sides)

    def __is_valid_color(self, r, g, b) -> bool:
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True
        return False

    def __is_valid_sides(self, *sides) -> bool:
        if self.sides_count == len(sides) and all(
            isinstance(side, int) and side > 0 for side in sides
        ):
            return True
        return False

    def get_color(self):
        return self.__color

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)
        else:
            print(f"Неверные значения цвета: {r} {g} {b}")

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = new_sides
        else:
            print(f"Неверные значения сторон: {new_sides}")


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides) -> None:
        Figure.__init__(self, color, *sides)
        self.__radius = self.get_sides()[0] / (2 * 3.14)

    def set_sides(self, *new_sides):
        Figure.set_sides(self, *new_sides)
        self.__radius = self.get_sides()[0] / (2 * 3.14)

    def get_square(self):
        return 3.14 * self.__radius**2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides) -> None:
        Figure.__init__(self, color, sides)

    def get_square(self):
        side_a, side_b, side_c = self.get_sides()
        s = (side_a + side_b + side_c) / 2
        area = math.sqrt(s * (s - side_a) * (s - side_b) * (s - side_c))
        return area


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides) -> None:
        if len(sides) == 1:
            sides = (sides[0],) * self.sides_count
        Figure.__init__(self, color, *sides)

    def get_volume(self):
        return self.get_sides()[0] ** 3

    def set_sides(self, *new_sides):
        if len(new_sides) == 1:
            new_sides = (new_sides[0],) * self.sides_count
        if len(new_sides) == self.sides_count and all(
            isinstance(side, int) and side == new_sides[0] for side in new_sides
        ):
            Figure.set_sides(self, *new_sides)
        else:
            print(f"Неверные значения сторон для куба: {new_sides}")


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)


# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

print(Circle((200, 200, 100), 10, 15, 6).get_sides())
print(Triangle((200, 200, 100), 10, 6).get_sides())
print(Cube((200, 200, 100), 9).get_sides())
print(Cube((200, 200, 100), 9, 12).get_sides())
