# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mielib']

package_data = \
{'': ['*']}

install_requires = \
['scipy>=1.9.3,<2.0.0']

setup_kwargs = {
    'name': 'mielib',
    'version': '0.1.8',
    'description': '',
    'long_description': '# MieLib\n\nPython library with many Mie-related functions for optics and acoustics. In particular:\n- Scattering Mie coefficients for isotropic spheres:\n    -  Acoustic Mie coefficients based on Phys. Rev. Lett. 123, 183901 (2019) (see SM)\n    - Optics Mie coefficients based on Bohren Huffmann book.\n- Scalar spherical harmonics\n- Vector spherical harmonics (complex and real)\n\n## Instalation\n\nFrom [PYPI/mielib](https://pypi.org/project/mielib/):\n```\npip install mielib\n```\n\n## Examples\n\nSee examples folder with Jupyter Notebooks.\n\n## ToDo\n\n* Make tests\n* Setup github actions\n* Search for complex poles of Mie scattering coefficients\n\n## Credits\nIvan Toftul \n\n`toftul.ivan@gmail.com`\n',
    'author': 'Ivan Toftul',
    'author_email': 'toftul.ivan@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
