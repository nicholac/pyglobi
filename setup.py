
import os
import sys
from setuptools import setup, find_packages

import twine

here = os.path.abspath(os.path.dirname(__file__))


if sys.argv[-1] == 'test':
    os.system('python -m pytest tests')
    sys.exit()

if sys.argv[-1] == 'build':
    os.system('python setup.py sdist bdist_wheel')
    sys.exit()

if sys.argv[-1] == 'publish':
    #os.system('python setup.py sdist bdist_wheel')
    #os.system('twine upload dist/*')
    print ('Skipping - not ready to upload yet')
    sys.exit()


with open("README.md", "r") as fh:
    long_description = fh.read()

# TODO
packages = ['pyglobi']

requires = [
    'requests>=2.22.0',
    'neo4j-driver>=1.7.6'
]

# TODO:
test_requirements = [
    'pytest>=3'
]

about = {}
with open(os.path.join(here, 'pyglobi', '__version__.py'), 'r') as f:
    exec(f.read(), about)

with open('README.md', 'r') as f:
    readme = f.read()
with open('HISTORY.md', 'r') as f:
    history = f.read()

setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    long_description=readme,
    long_description_content_type='text/markdown',
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)