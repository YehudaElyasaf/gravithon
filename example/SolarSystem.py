from gravithon.astronomy.Planets import *
from gravithon.Space import Space
from gravithon.Screen import Screen
from gravithon.units import time
from numpy import array, ndarray

DIMENSIONS = 2

# switch to 3d space class
# Create space
space = Space(dimensions=DIMENSIONS, fps=100)

# Add sun
space.add_body(Sun, array([0] * DIMENSIONS))
# Add planets
space.add_body(Mercury, Sun)
space.add_body(Venus, Sun)
space.add_body(Earth, Sun)
space.add_body(Mars, Sun)
space.add_body(Jupiter, Sun)
space.add_body(Saturn, Sun)
space.add_body(Uranus, Sun)
space.add_body(Pluto, Sun)
# Add moon
space.add_body(Moon, Earth)

print(space)
Screen(space, time=1*time.year_of_days, speed=1000000).show()
