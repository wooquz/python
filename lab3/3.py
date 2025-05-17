import math
from abc import ABC, abstractmethod

# Абстрактный класс Shape: задаёт интерфейс для всех фигур
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # площадь

    @abstractmethod
    def perimeter(self):
        pass  # периметр

class Rectangle(Shape):
    # Прямоугольник задаётся шириной и высотой
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height  # ширина * высота

    def perimeter(self):
        return 2 * (self.width + self.height)  # сумма сторон * 2

class Circle(Shape):
    # Круг задаётся радиусом
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2     # πr²

    def perimeter(self):
        return 2 * math.pi * self.radius    # 2πr

class Triangle(Shape):
    # Треугольник по трём сторонам (с Героновой формулой для площади)
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def area(self):
        p = (self.a + self.b + self.c) / 2   # полупериметр
        return math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))

    def perimeter(self):
        return self.a + self.b + self.c      # сумма сторон

# Демонстрация полиморфизма: любая фигура из Shape
def print_shape_info(shape: Shape):
    print(f"--- {shape.__class__.__name__} ---")
    print(f"Площадь:  {shape.area():.2f}")
    print(f"Периметр: {shape.perimeter():.2f}\n")

# Пример:
if __name__ == "__main__":
    shapes = [
        Rectangle(4, 5),    # прямоугольник 4×5
        Circle(3),          # круг радиусом 3
        Triangle(3, 4, 5)   # прямоугольный треугольник 3-4-5
    ]
    for sh in shapes:
        print_shape_info(sh)  # одинаковый вызов для разных классов