from gravithon.Sphere import Sphere
from gravithon.Space import Space
from numpy import array, ndarray

s = Space(2)
s1 = Sphere('s1', 3)
s2 = Sphere('and the second', 4, array([1, 2, 3]))
s.add_body(s1, array([4, 4]))
s.add_body(s2, array([5, 5]))
s1.move(array([10, 10]))
s2.accelerate(array([-1, -2]))
# s.remove_body(s2)
print(s)
