from numpy import ndarray, array


class Vector(ndarray):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)
