"""
    wg-federation build script
"""
from setuptools import setup
import pathlib
import os

pwd = pathlib.Path(__file__).parent.resolve()

constants_sourcefile = os.path.join(pwd, 'src/wg_federation/constants.py')
constants = {'__file__': constants_sourcefile}

with open(constants_sourcefile) as constants_module:
    exec(constants_module.read(), constants)

with open('src/wg_federation/__version__.txt', 'w') as version_file:
    version_file.write(constants['__version__'])

setup(
    # Versions should comply with PEP 440:
    # https://www.python.org/dev/peps/pep-0440/
    # https://packaging.python.org/guides/single-sourcing-package-version/
    version=constants['__version__'],
)
