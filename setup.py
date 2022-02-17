from setuptools import setup, find_packages

VERSION = '1.0.0'
DESCRIPTION = 'Converts images to ASCII art'

setup(
    name='asciify',
    version=VERSION,
    author='Braeden King',
    email='braedenking16@outlook.com',
    description=DESCRIPTION,
    packages=find_packages(),
    keywords=['python', 'ascii art', 'ascii'],
    classifiers=[
        'Programming Language :: Python :: 3'
    ]
)