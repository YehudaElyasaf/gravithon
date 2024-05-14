from gravithon.Sphere import Sphere
from gravithon.Line import Line
from gravithon.Space import Space
from gravithon.units.length import *
from gravithon.units.mass import *
from gravithon.astronomy.Planets import Earth
from gravithon.Screen import Screen
from gravithon.fields.GravitationalField import GravitationalField
from numpy import array, ndarray

DIMENSIONS = 2


def main():
    # Create space
    space = Space(dimensions=DIMENSIONS, fps=100)

    # Add bodies
    space.add_body(
        Sphere(
            name="Ball1",
            mass=1000000000000 * kg,
            radius=50 * cm,
            color='green'
        ),
        array([1 * m, 6 * m]))  # Position

    space.add_body(
        Sphere(
            name="Ball2",
            mass=1000000000000 * kg,
            radius=20 * cm,
            color='red'
        ),
        array([6 * m, 9 * m]))  # Position

    space.add_body(
        Line(
            name="Ground",
            slope=0,
            color='brown'
        )
        , array([0, 0])  # Position
    )

    # Add gravitational field (g)
    space.add_field(GravitationalField(
        array([0, -Earth.surface_gravity(), 0])
    ))

    # Print space info
    print(space)
    # Run space emulation
    Screen(space).show()


def TODOdelete():
    # Create space
    space = Space(dimensions=DIMENSIONS, fps=100)

    # Add bodies
    space.add_body(
        Sphere(
            name="Ball1",
            mass=10 * kg,
            radius=50 * cm,
            color='green'
        ),
        array([1 * m, 6 * m]),
        array([3, 4])
    )  # Position

    space.add_body(
        Sphere(
            name="Ball2",
            mass=10 * kg,
            radius=20 * cm,
            color='red'
        ),
        array([6 * m, 9 * m]))  # Position

    space.add_body(
        Line(
            name="Ground",
            slope=0,
            color='brown'
        )
        , array([0, 0])  # Position
    )

    # Add gravitational field (g)
    space.add_field(GravitationalField(
        array([0, -Earth.surface_gravity(), 0])
    ))

    # Print space info
    print(space)
    # Run space emulation
    Screen(space, speed=0.2).show()


if __name__ == '__main__':
    TODOdelete()
