from gravithon.Body import Body
from abc import ABC, abstractmethod
from gravithon import formulas


class Body3D(Body, ABC):
    def __init__(self, name: str, mass: float, color: str = None):
        super().__init__(name, 3, mass, color)

    def __str__(self):
        return super().__str__() + \
            ('' if self.volume() is None else '\n' + f'  Volume: {self.volume()} m^3')

    @property
    @abstractmethod
    def two_dimensional(self):
        pass

    @property
    def x(self):
        return self.position[0]

    @property
    def y(self):
        return self.position[1]

    @property
    def z(self):
        return self.position[2]

    @abstractmethod
    def volume(self):
        pass

    def density(self):
        return formulas.density(self.mass, self.volume())
