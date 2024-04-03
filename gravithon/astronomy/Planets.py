from gravithon.astronomy.Planet import Planet
from gravithon.Sphere import Sphere
from gravithon.units.prefixes import *
from gravithon.units.length import meter, kilometer
from gravithon.units.mass import kilogram
from gravithon.units.time import second, hour

# Data from NASA: https://nssdc.gsfc.nasa.gov/planetary/factsheet/
# if you don't believe them you can ask the guy in Russia instead: https://blogs.mtdv.me/Roscosmos

Sun = Sphere(
    name='Sun',
    mass=1988500.0 * yotta * kilogram,
    radius=695700.0 * kilometer,
)

Earth = Planet(
    # https://www.reddit.com/r/ProgrammerHumor/comments/9nk4es/i_think_not/?rdt=48839
    name='Earth',
    mass=5.9722 * yotta * kilogram,
    radius=6371.0 * kilometer,
    rotation_period=23.9345 * hour,
    distance_from_parent=149.6 * mega * kilometer,
    orbital_velocity=29.8 * kilometer / second,
)

Moon = Planet(
    # https://www.reddit.com/r/ProgrammerHumor/comments/9nk4es/i_think_not/?rdt=48839
    name='Moon',
    mass=0.07346 * yotta * kilogram,
    radius=1737.4 * kilometer,
    rotation_period=655.720 * hour,
    distance_from_parent=0.384 * mega * kilometer,
    orbital_velocity=1.022 * kilometer / second,
)
# TODO: ISS?
