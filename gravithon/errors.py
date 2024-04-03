class BodyNotFoundError(Exception):
    def __init__(self, name: str):
        message = f'Body "{name}" is not in space'
        super().__init__(message)


class BodyAlreadyExistError(Exception):
    def __init__(self, name: str):
        message = f'A body named "{name}" already exists in this space'
        super().__init__(message)


class DimensionsError(Exception):
    def __init__(self, body1_name: str, body1_dimensions: int, body2_name: str, body2_dimensions: int):
        message = f'{body1_name} has {body1_dimensions} dimensions, but {body2_name} has {body2_dimensions} dimensions'
        super().__init__(message)
