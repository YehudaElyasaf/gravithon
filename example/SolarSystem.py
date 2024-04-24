from gravithon.astronomy.Planets import *
from gravithon.Space import Space
from gravithon.Screen import Screen
from gravithon.units import time
from numpy import array, ndarray

DIMENSIONS = 2


def main():
    # Create space
    solar_system = Space(dimensions=DIMENSIONS)

    # Add sun
    solar_system.add_body(Sun, array([130000000000, 0]))
    # Add planets
    solar_system.add_body(Mercury, Sun)
    solar_system.add_body(Venus, Sun)
    solar_system.add_body(Earth, Sun)
    solar_system.add_body(Mars, Sun)
    solar_system.add_body(Jupiter, Sun)
    solar_system.add_body(Saturn, Sun)
    solar_system.add_body(Uranus, Sun)
    solar_system.add_body(Pluto, Sun)
    # Add moon
    solar_system.add_body(Moon, Earth)

    # Print space info
    print(solar_system)
    # Run space emulation
    Screen(solar_system, speed=1000000).show()


if __name__ == '__main__':
    main()
