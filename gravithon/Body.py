from abc import ABC, abstractmethod
from numpy import ndarray
from gravithon.errors import *


class Body(ABC):
    name: str
    mass: float
    position: ndarray
    velocity: ndarray

    def __init__(self, name: str, mass: float):
        # TODO: no mass bodies?
        self.name = name
        self.mass = mass
        self.position = None  # Body gets position when it's added to space
        self.velocity = None

    def __str__(self):
        # TODO: __str__ with other unit systems?
        return \
                self.name + ':\n' + \
                f'  Mass: {self.mass} kg' + '\n' + \
                f'  Position: {self.position}' + '\n' + \
                f'  Velocity: {self.velocity}' + '\n'

    def move(self, position: ndarray):
        # check dimensions
        if len(self.position) != len(position):
            raise DimensionsError(self.name + '\'s position', len(self.position), 'added position', len(position))

        self.position += position

    def accelerate(self, velocity: ndarray):
        # check dimensions
        if len(self.velocity) != len(velocity):
            raise DimensionsError(self.name + '\'s velocity', len(self.velocity), 'added velocity', len(velocity))

        self.velocity += velocity

    # TODO: calculate density
