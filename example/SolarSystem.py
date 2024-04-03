from gravithon.astronomy.Planets import *
from gravithon.Space import Space
from numpy import array, ndarray

# switch to 3d space class
# Create space
space = Space(3)

# Add sun
space.add_body(Sun, array([0, 0, 0]))
# Add planets
space.add_body(Earth, Sun)
# Add moon
space.add_body(Moon, Earth)
# TODO: run system
print(space)
