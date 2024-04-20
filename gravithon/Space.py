from gravithon.Body import Body
from gravithon.errors import *
from gravithon.astronomy.Satellite import Satellite
from multipledispatch import dispatch
from numpy import array, ndarray, copy


class Space:
    def __init__(self, dimensions: int = 3, background_color: str = 'black'):
        self.bodies = []
        self.time = 0.0
        self.dimensions = dimensions
        self.background_color = background_color

    def __str__(self):
        string = ''

        # bodies count
        if len(self.bodies) == 0:
            string += f'No bodies\n'
        elif len(self.bodies) == 1:
            string += f'1 body:\n'
        else:
            string += f'{len(self.bodies)} bodies:\n'

        # bodies
        for body in self.bodies:
            # indent body's string
            for line in str(body).split('\n'):
                string += '  ' + line + '\n'

            string += '\n'

        # time
        string += f'Time: {self.time}'

        return string

    @dispatch(Body, ndarray, ndarray)
    def add_body(self, body: Body, position: ndarray, velocity: ndarray):
        # check dimensions
        if len(position) != self.dimensions:
            # dimensions doesn't match
            raise DimensionsError('Space', self.dimensions, body.name + '\'s position', len(position))

        if velocity is not None and len(velocity) != self.dimensions:
            raise DimensionsError('Space', self.dimensions, body.name + '\'s velocity', len(velocity))

        # check if body has been already added
        for existing_body in self.bodies:
            if body.name == existing_body.name:
                raise BodyAlreadyExistError(body.name)

        # add body
        body.position = position.copy()
        body.velocity = velocity.copy()

        self.bodies.append(body)

    @dispatch(Body, ndarray)
    def add_body(self, body: Body, position: ndarray):
        velocity = array([0] * self.dimensions)  # zero velocity
        self.add_body(body, position, velocity)

    @dispatch(Satellite, Body)
    def add_body(self, satellite: Satellite, parent: Body):
        """
        Add satellite in orbit around a parent
        """
        # check if sun is in space
        try:
            self.bodies.index(parent)
        except ValueError:
            raise BodyNotFoundError(parent.name)

        # set position and velocity relative to parent
        position = parent.position.copy()
        position[0] += satellite.orbital_radius  # e.g. (in 3d spaces): [px+r py pz]
        velocity = array([0] * self.dimensions)
        velocity[0] += satellite.orbital_velocity  # e.g. (in 3d spaces): [v 0 0]

        if isinstance(satellite, Body):
            self.add_body(satellite, position, velocity)
        else:
            raise Exception('Satellite must be a body in order to be added to a space')

    @dispatch(Body)
    def remove_body(self, body):
        try:
            self.bodies.remove(body)
        except ValueError:
            raise BodyNotFoundError(body.name)

    @dispatch(str)
    def remove_body(self, body_name):
        # find body in bodies list
        try:
            body: Body = next(body for body in self.bodies if body.name == body_name)
        except StopIteration:
            raise BodyNotFoundError(body_name)

        self.remove_body(body)

    def step(self):
        raise NotImplementedError()  # TODO


# 2d space
class Plane(Space):
    def __init__(self):
        super().__init__(dimensions=2)
