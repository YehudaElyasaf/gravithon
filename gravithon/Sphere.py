from gravithon.Body import *
from gravithon.Circle import Circle
from gravithon.errors import *
from numpy import pi


class Sphere(Body3D):
    def __init__(self, name: str, mass: float, radius: float, color: str = None):
        super().__init__(name, mass, color)

        NonPositiveValueError.validate_positivity(radius)
        self.radius = float(radius)

    def __str__(self):
        return super().__str__() + \
            '\n' + \
            f'  Radius: {self.radius} m'

    def volume(self):
        return (4 / 3) * pi * (self.radius ** 3)

    def to_2d(self):
        return Circle(self.name, self.mass, self.radius, self.color)
