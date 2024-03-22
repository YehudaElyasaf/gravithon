from setuptools import setup, find_packages
from gravithon.version import __version__

with open('README.md') as file:
    long_description = file.read()

setup(
    name='gravithon',
    version=__version__,
    packages=find_packages(),
    url='https://github.com/YehudaElyasaf/gravithon',
    license='MIT',
    author='Yehuda Elyasaf',
    author_email='30yehuda26@gmail.com',
    description='d',  # TODO
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
