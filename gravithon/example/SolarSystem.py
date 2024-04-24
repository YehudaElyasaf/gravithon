from gravithon.astronomy.Planets import *
from gravithon.Space import Space
from gravithon.Screen import Screen
from gravithon.units import time
from numpy import array, ndarray

DIMENSIONS = 2


class SolarSystem(Space):
    def __init__(self):
        super().__init__(DIMENSIONS)

        # Add sun
        self.add_body(Sun, array([130000000000, 0]))
        # Add planets
        self.add_body(Mercury, Sun)
        self.add_body(Venus, Sun)
        self.add_body(Earth, Sun)
        self.add_body(Mars, Sun)
        self.add_body(Jupiter, Sun)
        self.add_body(Saturn, Sun)
        self.add_body(Uranus, Sun)
        self.add_body(Pluto, Sun)
        # Add moon
        self.add_body(Moon, Earth)

    def run(self):
        print(self)
        Screen(self, speed=1000000).show()


if __name__ == '__main__':
    SolarSystem().run()
