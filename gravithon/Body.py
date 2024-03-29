from abc import ABC, abstractmethod
from numpy import ndarray


class Body(ABC):
    name: str
    mass: float
    position: ndarray
    velocity: ndarray

    @abstractmethod
    def move(self, position):
        pass

    @abstractmethod
    def accelerate(self, velocity):
        pass

    def __str__(self):
        return \
                self.name.upper() + '\n' + \
                '-' * len(self.name) + '\n' + \
                f'Mass: {self.mass}' + '\n' + \
                f'Position: {self.position}' + '\n' + \
                f'Velocity: {self.velocity}'
