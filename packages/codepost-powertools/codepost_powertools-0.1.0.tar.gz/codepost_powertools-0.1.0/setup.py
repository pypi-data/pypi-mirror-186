# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['codepost_powertools',
 'codepost_powertools._utils',
 'codepost_powertools.grading',
 'codepost_powertools.utils']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'codepost>=0.2.29,<0.3.0',
 'comma>=0.5.4,<0.6.0',
 'loguru>=0.6.0,<0.7.0']

extras_require = \
{':python_version < "3.8"': ['importlib-metadata>=1.0']}

entry_points = \
{'console_scripts': ['cptools = codepost_powertools.__main__:cli']}

setup_kwargs = {
    'name': 'codepost-powertools',
    'version': '0.1.0',
    'description': 'Some helpful codePost tools to aid with grading flow.',
    'long_description': 'codePost Powertools\n===================\n\n.. badges\n\n.. image:: https://readthedocs.org/projects/codepost-powertools/badge/?version=latest\n   :target: https://codepost-powertools.readthedocs.io/en/latest/?badge=latest\n   :alt: Documentation Status\n\n.. |codePost SDK| replace:: ``codePost`` SDK\n.. _codePost SDK: https://github.com/codepost-io/codepost-python\n\nSome helpful codePost tools to aid with grading flow using the |codePost SDK|_!\n\nThese tools were originally created to support the grading process for COS126,\nthe introductory Computer Science course at Princeton University.\n\n.. end-intro\n\nDocumentation\n-------------\n\nThe documentation can be found\n`here <https://codepost-powertools.readthedocs.io/en/latest/>`_.\n\n.. The "Overview" page in the documentation is a more detailed version of the\n   below. Note that it does not use it directly, since this file must be PyPi-\n   compliant. See:\n   https://packaging.python.org/en/latest/guides/making-a-pypi-friendly-readme/#validating-restructuredtext-markup\n\nInstallation\n------------\n\n.. code-block:: bash\n\n   $ pip install codepost-powertools\n\nUsage\n-----\n\nPlease see the documentation for a more detailed description of the usage.\n\nYou should have a dedicated folder for the usage of these tools, since it\nrequires an input config file and outputs files for certain commands /\nfunctions. It is recommended to use a virtual environment for this:\n\n.. code-block:: bash\n\n   $ python -m venv env\n   $ source env/bin/activate\n   (env) $ python -m pip install codepost-powertools\n   (env) $ cptools --help\n   (env) $ python my_script.py\n\nBy default, the package will look for a configuration file called\n``config.yaml`` that contains a field ``"api_key"`` for your codePost API key.\nSee\n`this page <https://docs.codepost.io/docs#2-obtaining-your-codepost-api-key>`_\nfor instructions on how to access your codePost API key, as well as more\ninformation on the config YAML file. You must have admin access to all the\ncourses you wish to access with this package.\n\nCommand Line Usage\n^^^^^^^^^^^^^^^^^^\n\nYou can access the command-line interface with the ``cptools`` command:\n\n.. code-block:: bash\n\n   $ cptools --help\n\n   Usage: cptools [OPTIONS] COMMAND [ARGS]...\n\n     The `codepost_powertools` package on the command line.\n\nPlease see the CLI documentation for more information.\n\nScript Usage\n^^^^^^^^^^^^\n\nYou can import the package in a script:\n\n.. code-block:: python\n\n   import codepost_powertools as cptools\n   \n   # Log in to codePost\n   cptools.log_in_codepost()\n\n   # Call methods\n\nPlease see the "Writing Scripts" documentation for more information.\n',
    'author': 'Joseph Lou',
    'author_email': 'jdlou@princeton.edu',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://codepost-powertools.readthedocs.io/en/latest/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7.2,<4.0.0',
}


setup(**setup_kwargs)
