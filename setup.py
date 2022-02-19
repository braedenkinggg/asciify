from setuptools import setup, find_packages
from io import open
from os import path

VERSION = '1.0.0'
README = 'README.md'

setup(
    name = 'asciify',
    description = 'A simple open-source python script that converts images to ASCII art',
    version = VERSION,
    packages = find_packages(),
    python_requires = '>=3.9',
    entry_points = '''
        [console_scripts]
        asciify=asciify.asciify:main
    ''',
    author = 'Braeden King',
    keywords = 'python, opencv, ascii-art,  ascii',
    long_description = README,
    long_description_content_type = 'text/markdown',
    license='GPL-2.0',
    url = 'https://github.com/braedenkinggg/asciify',
    download_url = 'https://github.com/braedenkinggg/asciify/archive/refs/heads/main.zip',
    author_email = 'braedenking16@outlook.com',
    classifiers = [
        'Programming Language :: Python :: 3.9'
    ]
)