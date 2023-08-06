# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['test_pypi_hfudev', 'tests']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'test-pypi-hfudev',
    'version': '1.0.0rc0',
    'description': 'Top-level package for test-pypi-hfudev.',
    'long_description': '================\ntest-pypi-hfudev\n================\n\n\n.. image:: https://img.shields.io/pypi/v/test_pypi_hfudev.svg\n        :target: https://pypi.python.org/pypi/test_pypi_hfudev\n\n.. image:: https://img.shields.io/travis/hfudev/test_pypi_hfudev.svg\n        :target: https://travis-ci.com/hfudev/test_pypi_hfudev\n\n.. image:: https://readthedocs.org/projects/test-pypi-hfudev/badge/?version=latest\n        :target: https://test-pypi-hfudev.readthedocs.io/en/latest/?badge=latest\n        :alt: Documentation Status\n\n\n\n\nA Python package to test pypi version solver\n\n\n* Free software: MIT\n* Documentation: https://test-pypi-hfudev.readthedocs.io.\n\n\nFeatures\n--------\n\n* TODO\n\nCredits\n-------\n\nThis package was created with Cookiecutter_ and the `briggySmalls/cookiecutter-pypackage`_ project template.\n\n.. _Cookiecutter: https://github.com/audreyr/cookiecutter\n.. _`briggySmalls/cookiecutter-pypackage`: https://github.com/briggySmalls/cookiecutter-pypackage\n',
    'author': 'Fu Hanxi',
    'author_email': 'hfudev@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/hfudev/test_pypi_hfudev',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4',
}


setup(**setup_kwargs)
