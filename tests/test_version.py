from gravithon import __version__


# check if version in pyproject.toml is updated
def test_version():
    with open('../pyproject.toml') as file:
        content = file.read()
        if __version__ not in content:
            raise Exception(f'Version is {__version__} but version in pyproject.toml is different:\n{content}')
