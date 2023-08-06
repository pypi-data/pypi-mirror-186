# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['philipstv', 'philipstv.model']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.9.0,<2.0.0', 'requests>=2.27.1,<3.0.0']

extras_require = \
{'cli': ['click>=8.0.3,<9.0.0', 'appdirs>=1.4.4,<2.0.0'],
 'docs': ['Sphinx>=4.4.0,<5.0.0',
          'furo>=2022.2.14,<2023.0.0',
          'enum-tools[sphinx]>=0.9.0,<0.10.0']}

entry_points = \
{'console_scripts': ['philipstv = philipstv.__main__:wrapped_cli']}

setup_kwargs = {
    'name': 'philipstv',
    'version': '1.1.0',
    'description': 'CLI and library to control Philips Android-powered TVs.',
    'long_description': "philipstv\n=========\n\n.. image:: https://github.com/bcyran/philipstv/workflows/CI/badge.svg?event=push\n   :target: https://github.com/bcyran/philipstv/actions?query=event%3Apush+branch%3Amaster+workflow%3ACI\n   :alt: CI\n\n.. image:: https://codecov.io/gh/bcyran/philipstv/branch/master/graph/badge.svg?token=ROJONX34RB\n   :target: https://codecov.io/gh/bcyran/philipstv\n   :alt: codecov\n\n.. image:: https://img.shields.io/badge/code%20style-black-000000.svg\n   :target: https://github.com/psf/black\n   :alt: Code style: black\n\n.. image:: https://img.shields.io/pypi/v/philipstv\n   :target: https://pypi.org/project/philipstv/\n   :alt: pypi\n\n.. image:: https://readthedocs.org/projects/philipstv/badge/?version=latest\n   :target: https://philipstv.readthedocs.io/en/latest/?badge=latest\n   :alt: Documentation status\n\n.. image:: https://img.shields.io/pypi/pyversions/philipstv\n   :target: https://pypi.org/project/philipstv/\n   :alt: versions\n\n.. image:: https://img.shields.io/github/license/bcyran/philipstv\n   :target: https://github.com/bcyran/philipstv/blob/master/LICENSE\n   :alt: license\n\n.. -begin-intro-\n\nPython package providing CLI and library for interacting with Philips Android-powered TVs.\n\nFeatures:\n\n- Get and set TV power state.\n- Get and set volume.\n- List and change TV channels.\n- Emulate pressing remote keys.\n- Get and set Ambilight power state.\n- Get and set Ambilight color.\n- List and launch applications.\n\nInstallation\n------------\n\nPyPI\n^^^^\n\nIf you plan to use the CLI:\n\n.. code-block:: console\n\n   $ pip install 'philipstv[cli]'\n\nIf you only need library for use in Python code:\n\n.. code-block:: console\n\n   $ pip install philipstv\n\n.. -end-intro-\n\nArch Linux (AUR)\n^^^^^^^^^^^^^^^^\n\n`philipstv AUR package <https://aur.archlinux.org/packages/philipstv>`_ is available.\n\n\nDocumentation\n-------------\nSee full documentation: `Read the Docs: philipstv <https://philipstv.readthedocs.io>`_.\n\nSee also\n--------\n- `PhilipsTV GUI <https://github.com/bcyran/philipstv-gui>`_ - GUI application built with this library.\n\nResources\n---------\n- `Fantastic unofficial API documentation <https://github.com/eslavnov/pylips/blob/master/docs/Home.md>`_ and `script <https://github.com/eslavnov/pylips>`_ by `@eslavnov <https://github.com/eslavnov>`_.\n- Philips `JointSpace API documentation <http://jointspace.sourceforge.net/projectdata/documentation/jasonApi/1/doc/API.html>`_.\n",
    'author': 'Bazyli Cyran',
    'author_email': 'bazyli@cyran.dev',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/bcyran/philipstv',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
