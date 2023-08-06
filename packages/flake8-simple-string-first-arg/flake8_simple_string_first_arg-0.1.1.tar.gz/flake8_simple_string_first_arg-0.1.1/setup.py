# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['flake8_simple_string_first_arg']
install_requires = \
['astpretty', 'flake8']

entry_points = \
{'flake8.extension': ['SFA = flake8_simple_string_first_arg:Plugin']}

setup_kwargs = {
    'name': 'flake8-simple-string-first-arg',
    'version': '0.1.1',
    'description': 'This Flake8 plugin for checking that first param of callable is simple string.',
    'long_description': '# flake8-simple-string-first-arg\n\nThis *Flake8* plugin for checking that first param of callable object is simple string. \nPlugin will check for specified callable objects that \nit is not allowed to use f-sting, .format method, string concat and % statement for first parameter\n\n# Quick Start Guide\n\n1. Install ``flake8-simple-string-first-arg`` from PyPI with pip::\n\n        pip install flake8-simple-string-first-arg\n\n2. Configure a mark that you would like to validate::\n\n        cd project_root/\n        vi setup.cfg\n\n3. Add to file following: \n   \n        [flake8]  \n        simple-string-first-arg = SomeClassName, OtherClassName:url\n\n3. Run flake8::\n\n        flake8 .\n\n# flake8 codes\n\n   * SFA100: In calling {CallableName} f-string is used\n   * SFA200: In calling {CallableName} string.format() is used\n   * SFA300: In calling {CallableName} string concatenation ("+") is used\n   * SFA400: In calling {CallableName} "%" is used\n\n# Settings\n\n**simple-string-first-arg**  \nIt specifies a list of name of callable objects, that should have simple string as first arg.\nYou can add the name of the argument via `:` to check if it is passed as a named parameter.\n',
    'author': 'Kozyar Valeriy',
    'author_email': 'monqpepers@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
