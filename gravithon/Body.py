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

    def __init__(self, name: str, mass: float = None, color: str = None):
        self.name = name
        if mass is not None:
            # bodies with no mass are allowed, bodies with zero mass aren't
            NegativeValueError.validate_negativity(mass)
        self.mass = mass
        self.position = None  # Body gets position when it's added to space
        self.velocity = None
        self.color = color

    def __str__(self):
        # TODO: better __str__ in all bodies?
        return \
                self.name + ':\n' + \
                f'  Mass: {self.mass} kg' + '\n' + \
                f'  Position: {self.position} m' + '\n' + \
                f'  Velocity: {self.velocity} m/s' + '\n' + \
                f'  Volume: {self.volume()} m^3' + '\n' + \
                f'  Density: {self.density()} kg/m^3'

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

    def gravitational_force(self, other: Body):
        return array([self.gravitational_field(self.distance(other)) * other.mass, 0.0, 0.0])

    def __total_gravitational_force(self, space_dimensions: int, bodies: list):
        force = array([0.0] * space_dimensions)

        # TODO: Field class
        for body in bodies:
            if body is not self:
                force += self.gravitational_force(body)

        return force

    def calculate_total_force(self, space_dimensions: int, bodies: list):
        return \
            self.__total_gravitational_force(space_dimensions, bodies)

    def calculate_acceleration(self, space_dimensions: int, bodies: list):
        F = self.calculate_total_force(space_dimensions, bodies)
        return formulas.acceleration(F, self.mass)
