from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Lorem ipsum...'

# Setting up
setup(
    name="pialgebra",
    version=VERSION,
    author="Pierre",
    author_email="pierre.bejian@gmail.com",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['numpy'],
    classifiers=[]
)
