import math
class Figure:
    sides_count = 0

    def __init__(self, color, sides, filled=False):
        if self.__is_valid_sides(*sides):
            if isinstance(self, Cube):
                self.__sides = list(sides) * self.sides_count
            else:
                self.__sides = list(sides)
        else:
            self.__sides = [1] * self.sides_count

        self.__color = list(color)
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        for color in [r, g, b]:
            if not (isinstance(color, int) and 0 <= color <= 255):
                return False
        return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        #cond_1 = len(self.__sides) == len(sides)
        if isinstance(self, Cube):
            cond_1 = len(sides) == 1
        else:
            cond_1 = len(sides) == self.sides_count
        cond_2 = all([isinstance(side, int) and side > 0 for side in sides])
        return cond_1 and cond_2

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            if isinstance(self, Cube):
                self.__sides = list(new_sides)*12
            else:
                self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color: tuple, *sides):
        super().__init__(color, sides)
        self.__radius = self.sides_count/2*math.pi

    def get_radius(self):
        return self.__radius

    def get_square(self):
        return math.pi * math.pow(self.__radius, 2)

class Triangle(Figure):
    sides_count = 3

    def __init__(self, color: tuple, *sides):
        super().__init__(color, sides)
        self.__height = (2*self.get_square())/(self.__len__()/2)

    def get_square(self):
        p = self.__len__()/2 #полупериметр
        s = math.sqrt(p*(p-self.sides)*(p-self.sides)*(p-self.sides))#формула герона
        return s


class Cube(Figure):
    sides_count = 12

    def __init__(self, color: tuple, *sides):
        super().__init__(color, sides)

    def get_volume(self):
        v = self.sides**3
        return v





circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())






