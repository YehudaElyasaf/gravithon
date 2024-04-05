from gravithon.Body import *


class Sphere(Body):
    def volume(self):
        return formulas.sphere_volume(self.radius)

    def __init__(self, name: str, mass: float, radius: float):
        super().__init__(name, mass)

        # TODO: check negativity (also for mass etc.), and add NegativeValueException
        self.radius = radius

    def __str__(self):
        # TODO: __str__ with other unit systems?
        return super().__str__() + \
            '\n' + \
            f'  Radius: {self.radius} m'
