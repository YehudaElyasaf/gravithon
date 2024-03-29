from gravithon.Body import *
from numpy import array, ndarray


class Sphere(Body):
    def __init__(self, name: str, mass: float, velocity: ndarray = array([0, 0, 0])):
        self.name = name
        self.mass = mass
        self.position = None  # Body gets position when it's added to space
        self.velocity = velocity

        self.radius = 10

    def move(self, position):
        self.position += position

    def accelerate(self, velocity):
        self.velocity += velocity
