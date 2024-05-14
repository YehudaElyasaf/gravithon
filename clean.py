from os import system


def clean():
    # delete build files
    system('rm -rf dist')
    system('rm -rf gravithon.egg-info')
    system('rm -rf build')
    system('rm -rf $(find . -type d -name __pycache__)')


if __name__ == '__main__':
    print('CLEANING...')
    clean()
