from numpy import array, ndarray
from gravithon.Body import Body


class Space:
    def __init__(self):
        self.bodies = []
        self.time = float(0)

    def add_body(self, body: Body, position: ndarray):
        # check if body has been already added
        for existing_body in self.bodies:
            if body.name == existing_body.name:
                raise Exception(f'A body named "{body.name}" already exists in this space')

        # add body
        body.position = position
        self.bodies.append(body)

    def __str__(self):
        string = ''

        # bodies
        string += f'{len(self.bodies)} BODIES:\n'
        for body in self.bodies:
            # indent body's string
            for line in str(body).split('\n'):
                string += '\t' + line + '\n'

            string += '\n'

        # time
        string += f'Time: {self.time}'

        return string
