from gravithon.Sphere import Sphere
from gravithon.Space import Space
from gravithon.units.length import *
from gravithon.units.mass import *
from gravithon.astronomy.Planets import Earth
from gravithon.Screen import Screen
from gravithon.fields.GravitationalField import GravitationalField
from numpy import array, ndarray

DIMENSIONS = 2

# switch to 3d space class
# Create space
space = Space(dimensions=DIMENSIONS, fps=40)

space.add_body(Sphere(
    "Ball1",
    3 * kg,
    50 * cm,
    color='green'
), array([1 * m, 6 * m]))

space.add_body(Sphere(
    "Ball2",
    1 * kg,
    20 * cm,
    color='red'
), array([5 * m, 9 * m]))

space.add_field(GravitationalField(
    array([0, -Earth.surface_gravity(), 0])
))

print(space)
Screen(space).play()
