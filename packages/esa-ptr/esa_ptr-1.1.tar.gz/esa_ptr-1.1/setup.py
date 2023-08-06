# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['ptr', 'ptr.agm', 'ptr.block', 'ptr.datetime']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['juice-agm = ptr.cli:cli_juice_agm']}

setup_kwargs = {
    'name': 'esa-ptr',
    'version': '1.1',
    'description': 'ESA Planning Timeline Request package',
    'long_description': 'ESA Planning Timeline Request (PTR) Python package\n==================================================\n\nSince the [Rosetta mission](https://www.esa.int/Science_Exploration/Space_Science/Rosetta),\nESA developed an XML-like syntax to create Planning Timeline Request (PTR) files.\nThese files allow the mission team member to design custom attitude spacecraft pointing.\nIt is readable by `AGM` and `MAPPS` softwares to detect spacecraft constrains violations,\npower conception and surface coverage. It can also be used to compute custom spacecraft\nattitude (quaterions and `ck`).\nThis format will be re-used for the [JUICE mission](https://sci.esa.int/web/juice),\nand can already be tested on the [JUICE pointing tool](https://juicept.esac.esa.int).\n\nThis python package implements an object oriented approach to help the creation and parsing\nof PTR files for the user, as well an interface to check JUICE PTR validity with AGM.\n\n> **Disclaimer:** This package is an early release and does not support all PTR implementations.\n> Please, open an issue to report any issue you may accounter.\n> Currently this tool in **beta stage, do not use it in critical environments**.\n\nA detailed documentation can be found [here](https://esa-ptr.readthedocs.io/).\n\nInstallation\n------------\n\nThis package is available on [PyPI](https://pypi.org/project/esa-ptr/) and could be installed like this:\n\n```bash\npython -m pip install esa-ptr\n```\n\nEven if this tool does not have any external dependencies, we recommend to use it in an isolated virtual environment (`venv` or `conda`).\n\n\nDevelopment and testing\n-----------------------\n\nIf you want contribute to the development and tests your changes before submitting a merge request,\nyou need to install [Poetry](https://python-poetry.org/docs/) and clone this repository:\n\n```bash\ngit clone https://juigitlab.esac.esa.int/python/ptr.git python-esa-ptr ;\ncd python-esa-ptr/\n```\n\nInstall the package and its dependencies:\n```\npoetry install\n```\n\nThen, after your edits, you need to check that both linters are happy:\n```bash\npoetry run flake8\npoetry run pylint ptr tests/\n```\n\nand all the tests passed:\n```bash\npoetry run pytest\n```\n\n\nDocumentation\n-------------\n* Rosetta Flight Dynamics: `RO-ESC-IF-5501_i3r4_RSGS_FD_ICD-2.pdf`\n',
    'author': 'Benoît Seignovert',
    'author_email': 'benoit.seignovert@univ-nantes.fr',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://juigitlab.esac.esa.int/python/ptr',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
