from gravithon import formulas
from gravithon.fields.GravitationalField import GravitationalField
from gravithon.errors import *
from abc import ABC, abstractmethod

import numpy as np
from numpy import array, ndarray


class Body(ABC):
    name: str
    dimensions: int
    mass: float
    position: ndarray
    velocity: ndarray
    color: str

    def __init__(self, name: str, dimensions: int, mass: float, color: str = None):
        self.name = name
        self.dimensions = dimensions

        if mass is None:
            self.mass = None
        else:
            NonPositiveValueError.validate_positivity(mass)
            self.mass = float(mass)

        self.position = None  # Body gets position when it's added to space
        self.velocity = None
        self.color = color

    def __str__(self):
        return \
                self.name + ':\n' + \
                f'  Dimensions: {self.dimensions}' + '\n' + \
                ('' if self.mass is None else f'  Mass: {self.mass} kg' + '\n') + \
                f'  Position: {self.position} m' + '\n' + \
                f'  Velocity: {self.velocity} m/s'

    def move(self, velocity: ndarray):
        # check dimensions
        if len(self.position) != len(velocity):
            raise DimensionsError(self.name + '\'s position', len(self.position), 'velocity', len(velocity))

        self.position += velocity

    def accelerate(self, acceleration: ndarray):
        # check dimensions
        if len(self.velocity) != len(acceleration):
            raise DimensionsError(self.name + '\'s velocity', len(self.velocity), 'acceleration', len(acceleration))

        self.velocity += acceleration

    def collide(self, other: 'Body'):
        # check if bodies are in space
        if self.position is None:
            raise BodyNotInSpaceError(self.name)
        if other.position is None:
            raise BodyNotInSpaceError(other.name)

        # check dimensions
        if self.dimensions != other.dimensions:
            raise DimensionsError(self.name, self.dimensions, other.name, other.dimensions)

        # check if body has to move
        if self.mass is None or \
                not self.is_touching(other):
            return

        # check collision between bodies
        relative_velocity = self.velocity  # - other.velocity  # self velocity relative to other body TODO: needed?

        normal_unit = other._normal(self) / np.linalg.norm(other._normal(self))
        dot = np.dot(relative_velocity, normal_unit)
        reflected_velocity = relative_velocity - 2 * dot * normal_unit

        self.velocity = reflected_velocity  # TODO: test, decide velocity magnitude

    @abstractmethod
    def distance(self, other: 'Body'):
        pass

    @abstractmethod
    def _normal(self, other: 'Body'):
        """
        Calculate normal vector of collision plane between two bodies
        :param other: collapsed body
        :return: normal
        """
        pass

    def gravitational_field(self, distance: float):
        return formulas.gravitational_field(self.mass, distance)

    def gravitational_force(self, other: 'Body'):
        # set force direction
        force = []
        for i in range(self.dimensions):
            axis_distance = formulas.distance(self.position[i], other.position[i])
            force.append(axis_distance)
        force = array(force)

        # set force magnitude
        current_magnitude = formulas.magnitude(force)
        real_magnitude = self.gravitational_field(self.distance(other)) * other.mass

        force *= -(real_magnitude / current_magnitude)

        return force

    @abstractmethod
    def is_touching(self, other: 'Body'):
        pass

    def calculate_total_force(self, space_dimensions: int, bodies: list, fields: list):
        force = array([0.0] * space_dimensions)

        for body in bodies:
            if body is not self \
                    and body.mass is not None:
                force += self.gravitational_force(body)

        for field in fields:
            if isinstance(field, GravitationalField):
                force += field.value * self.mass
            else:
                raise FieldNotSupportedError(field)

        return force

    def calculate_acceleration(self, space_dimensions: int, bodies: list, fields: list):
        F = self.calculate_total_force(space_dimensions, bodies, fields)
        return formulas.acceleration(F, self.mass)
