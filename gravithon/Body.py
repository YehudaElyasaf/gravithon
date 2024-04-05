from __future__ import annotations
from gravithon import formulas
from abc import ABC, abstractmethod
from gravithon.errors import *
from numpy import array, ndarray


class Body(ABC):
    name: str
    mass: float
    position: ndarray
    velocity: ndarray

    def __init__(self, name: str, mass: float):
        self.name = name
        self.mass = mass
        self.position = None  # Body gets position when it's added to space
        self.velocity = None

    def __str__(self):
        # TODO: __str__ with other unit systems?
        return \
                self.name + ':\n' + \
                f'  Mass: {self.mass} kg' + '\n' + \
                f'  Position: {self.position} m' + '\n' + \
                f'  Velocity: {self.velocity} m/s' + '\n' + \
                f'  Volume: {self.volume()} m^3' + '\n' + \
                f'  Density: {self.density()} kg/m^3'
        # TODO: acceleration`

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

    @abstractmethod
    def volume(self):
        pass

    def density(self):
        return formulas.density(self.mass, self.volume())

    def distance(self, other: Body):
        return formulas.distance(self.position, other.position)

    def gravitational_field(self, distance: float):
        return formulas.gravitational_field(self.mass, distance)

    def gravity(self, other: Body):
        return self.gravitational_field(self.distance(other)) * other.mass
