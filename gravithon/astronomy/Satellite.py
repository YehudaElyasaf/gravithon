from gravithon.Sphere import Sphere
from gravithon.units.prefixes import *
from gravithon.units.length import meter, kilometer
from gravithon.units.mass import kilogram
from gravithon.units.time import hour


class Satellite(Sphere):
    def __init__(self, name: str, mass: float, radius: float,
                 rotation_period: float, day_length: float, distance_from_sun: float, orbital_velocity: float,
                 satellites=None):
        super().__init__(name, mass, radius)

        if satellites is None:
            satellites = []

    # TODO: defs for orbital_period (Year), __str__, Surface gravity


# Data from NASA: https://nssdc.gsfc.nasa.gov/planetary/factsheet/
# if you don't believe them you can ask the guy in Russia instead: https://blogs.mtdv.me/Roscosmos
Moon = 'a'  # TODO: all planets, uncomment line in earth

Earth = Satellite(
    # https://www.reddit.com/r/ProgrammerHumor/comments/9nk4es/i_think_not/?rdt=48839
    name='Earth',
    mass=5.9722 * yotta * kilogram,
    radius=6378.137 * kilometer,
    rotation_period=23.9 * hour,
    day_length=24.0 * hour,
    distance_from_sun=149.6 * mega * meter,
    orbital_velocity=29.8,
    satellites=[Moon]
)
