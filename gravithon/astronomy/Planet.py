from gravithon.Sphere import Sphere
from gravithon.astronomy.Satellite import Satellite


class Planet(Sphere, Satellite):
    # radius is volumetric mean radius
    def __init__(self, name: str, mass: float, radius: float,
                 rotation_period: float, distance_from_parent: float, orbital_velocity: float):
        # sphere init
        Sphere.__init__(self, name, mass, radius)
        # satellite init
        Satellite.__init__(self, rotation_period, distance_from_parent, orbital_velocity)

    def __str__(self):
        return Sphere.__str__(self) + \
            Satellite.__str__(self) + \
            f'  Surface Gravity: {self.surface_gravity()} sec' + '\n'

    def surface_gravity(self):
        return self.gravitational_field(self.radius)
