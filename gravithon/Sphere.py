from gravithon.Body import *


class Sphere(Body):
    def __init__(self, name: str, mass: float, radius: float):
        super().__init__(name, mass)

        # TODO: check negativity (also for mass etc.)
        self.radius = radius

    def __str__(self):
        # TODO: __str__ with other unit systems?
        return super().__str__() + \
            f'  Radius: {self.radius} m' + '\n'
