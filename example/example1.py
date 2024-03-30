from gravithon.Sphere import Sphere
from gravithon.Space import Space
from gravithon.astronomy.Satellite import Earth
from numpy import array, ndarray

s = Space(2)
s1 = Sphere('sphere1', 3, radius=10)
s2 = Sphere('sphere2', 4, radius=20.3)
s.add_body(s1, array([4, 4]), array([33, 45]))
s.add_body(s2, array([5, 5]))
s1.move(array([10, 10]))
s2.accelerate(array([-1, -2]))
s.remove_body(s2)
s.add_body(Earth, array([0, 0]))

print(s)
