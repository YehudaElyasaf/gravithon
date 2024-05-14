from gravithon.Body import Body
from abc import ABC, abstractmethod


class Body2D(Body, ABC):
    def __init__(self, name: str, mass: float, color: str = None):
        super().__init__(name, 2, mass, color)

    def __str__(self):
        return super().__str__() + \
            ('' if self.area() is None else '\n' + f'  Area: {self.area()} m^2')

    @property
    def x(self):
        return self.position[0]

    @property
    def y(self):
        return self.position[1]

    @abstractmethod
    def area(self):
        pass
