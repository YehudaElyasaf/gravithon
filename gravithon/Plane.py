from gravithon.Line import *
from gravithon.Sphere import *
from gravithon.errors import *


class Plane(Body3D):
    def __init__(self, name: str,
                 A: float, B: float, C: float,
                 color: str = None):
        super().__init__(name, None, color)

        self.A = A
        self.B = B
        self.C = C

        # two-dimensional form is the intersection with YZ plane
        # 0x + By + Cz = D    =>    z = -By + D (D isn't yet set)
        # using this form isn't recommended, consider using Line class instead
        self.__two_dimensional = Line(self.name, -B, self.color)

    @property
    def D(self):
        if self.position is None:
            return
        # calculate the perpendicular distance of the plane from the origin
        x, y, z = self.position[0], self.position[1], self.position[2]

        # D = Ax + By + Cz
        return self.A * x + self.B * y + self.C * z

    def __str__(self):
        return super().__str__() + \
            '\n' + \
            f'  Equation: {self.A}x + {self.B}y + {self.C}z = {"D" if self.position is None else self.D}'

    @property
    def two_dimensional(self):
        return self.__two_dimensional

    def volume(self):
        # plane has no volume
        return None

    def normal(self):
        return array([self.A, self.B, self.C])

    def _normal(self, other: Body):
        return self.normal()

    def is_touching(self, other: Body):
        distance = self.distance(other)  # also checks dimensions

        if isinstance(other, Plane):
            self_normal_unit = self.normal() / np.linalg.norm(self.normal())
            other_normal_unit = other.normal() / np.linalg.norm(other.normal())

            if self_normal_unit != other_normal_unit:
                # not parallel, necessarily intersect
                return True

            elif self.D == other_normal_unit.D:
                # same plane
                return True
            else:
                return False

        elif isinstance(other, Sphere):
            return distance <= other.radius

        else:
            raise BodyNotSupportedError(other)

    def distance(self, other: Body):
        if not isinstance(other, Body3D):
            raise DimensionsError(self.name, self.dimensions, other.name, other.dimensions)

        if isinstance(other, Sphere):
            return formulas.distance_between_point_and_plane(other.position[0], other.position[1], other.position[2],
                                                             self.A, self.B, self.C, self.D)

        elif isinstance(other, Plane):
            # there is no distance between two planes (unless they are parallel)
            raise Exception('Can\'t calculate distance between two planes')

        else:
            raise BodyNotSupportedError(other)
