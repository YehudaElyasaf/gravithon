from get_pypi_latest_version import GetPyPiLatestVersion


# check if version in pyproject.toml has been increased
def verify_version():
    pypi_version = GetPyPiLatestVersion()('gravithon')
    with open('pyproject.toml') as file:
        content = file.read()

    # compare versions
    if pypi_version in content:
        # versions identical
        raise Exception(f'PyPI version ({pypi_version}) hasn\'t been increased in pyproject.toml')
