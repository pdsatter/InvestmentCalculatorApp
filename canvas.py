from abc import ABC

class Canvas(ABC):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.canvas = None

    def draw_circle(self, x, y, radius, outline="black", fill="blue"):
        ...

    def draw_square(self, x, y, width, outline="black", fill="blue"):
        ...

    def draw_triangle(self, x, y, width, outline="black", fill="blue"):
        ...
