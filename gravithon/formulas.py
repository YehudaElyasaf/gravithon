from gravithon.constants.astrophisics import *
from gravithon.Body import *
from math import sqrt, pi
from numpy import array, ndarray
from multipledispatch import dispatch


@dispatch(float, float, float)
def gravity(m1: float, m2: float, r: float):
    return (G * m1 * m2) / (r ** 2)


@dispatch(Body, Body)
def gravity(b1: Body, b2: Body):
    return gravity(b1.mass, b2.mass, distance(b1, b2))


@dispatch(ndarray, ndarray)
def distance(p1, p2):
    return p1 - p2


@dispatch(Body, Body)
def distance(b1: Body, b2: Body):
    return distance(b1.position, b2.position)


def orbital_period(r: float, v: float):
    """
    Calculate the amount of time a satellite takes to complete one orbit around it's parent
    :param r: radius - distance from parent
    :param v: orbital speed
    :return: period time [seconds]
    """
    return (2 * pi * r) / (v)


def gravitational_field(m: float, r: float):
    """
    Calculate the gravitational field's magnitude of an object in specific distance
    :param m: mass
    :param r: radius - distance from mass center
    :return: field
    """
    return (G * m) / (r ** 2)
