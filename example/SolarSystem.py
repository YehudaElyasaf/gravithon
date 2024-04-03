from gravithon.astronomy.Planets import *
from gravithon.Space import Space
from numpy import array, ndarray

# switch to 3d space class
# Create space
space = Space(3)

# Add sun
space.add_body(Sun, array([0, 0, 0]))
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
# TODO: run system
print(space)
