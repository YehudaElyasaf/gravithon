from gravithon.Body import *
from gravithon.errors import *
from numpy import pi


class Circle(Body2D):
    def __init__(self, name: str, mass: float, radius: float, color: str = None):
        super().__init__(name, mass, color)

        NonPositiveValueError.validate_positivity(radius)
        self.radius = float(radius)

    def __str__(self):
        return super().__str__() + \
            '\n' + \
            f'  Radius: {self.radius} m'

    def area(self):
        return pi * (self.radius ** 2)
