from math import pi


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__sides = list(sides)
        self.__color = list(color)
        self.filled = True

    def get_color(self):
        return self.__color

    def __is_valid_color(self, color):
        result = True
        for component in color:
            if not isinstance(component, int):
                result = False
        for component in color:
            if component < 0 or component > 255:
                result = False
        return result

    def set_color(self, *color):
        if self.__is_valid_color(color):
            self.__color = list(color)

    def __is_valid_sides(self, sides):
        result = True
        if len(self.__sides) != len(sides):
            result = False
        for side in sides:
            if (not isinstance(side, int)) or (side <= 0):
                result = False
        return result

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            if self.__is_valid_sides(new_sides):
                self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        if len(sides) != self.sides_count:
            sides = [1]
        super().__init__(color, *sides)
        self.radius = self.get_sides()[0] / (2 * pi)

    def get_square(self):
        return pi * (self.radius**2)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        if len(sides) != self.sides_count:
            sides = [1]*self.sides_count
        super().__init__(color, *sides)
        self.__height = 2 * self.get_square()/max(sides)

    def get_square(self):
        a, b, c = self.get_sides()
        p_per = sum(self.get_sides()) / 2
        return (p_per * (p_per - a) * (p_per - b) * (p_per - c)) ** 0.5


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) != 1:
            sides = [1] * self.sides_count
        else:
            sides = [sides[0]] * self.sides_count
        super().__init__(color, *sides)
        self.set_sides(sides[0])

    def get_volume(self):
        return self.get_sides()[0]**3


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

# Дополнительная проверка для треугольника. Основание считается к наибольшей стороне!
Triang1 = Triangle((200, 200, 100), 3, 4, 5)
print(f'Triangle with sides {Triang1.get_sides()}')
print(f'Max side : {max(Triang1.get_sides())}\nSquare :{Triang1.get_square()}\nHeight :{Triang1._Triangle__height}')
