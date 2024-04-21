from gravithon.Body import *
from gravithon.errors import *


class Line(Body2D):
    # y=ax+b
    def __init__(self, name: str, mass: float,
                 slope: float,
                 color: str = None):
        super().__init__(name, mass, color)

        self.slope = slope

    def __str__(self):
        return super().__str__() + \
            '\n' + \
            f'  Equation:  y = {self.slope}x + {"b" if self.position is None else self.y_intercept()}'

    def area(self):
        # line has no area
        return None

    def y_intercept(self):
        if self.position is None:
            raise Exception('Line has no position')
        else:
            # b=y-ax
            x = self.position[0]
            y = self.position[1]
            return y - self.slope * x

    def solve(self, x):
        # y=ax+b
        return self.slope * x + self.y_intercept()
