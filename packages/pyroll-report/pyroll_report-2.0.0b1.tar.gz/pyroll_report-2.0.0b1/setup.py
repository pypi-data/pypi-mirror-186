# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['report', 'report.unit_display']

package_data = \
{'': ['*']}

install_requires = \
['Jinja2>=3.0.3,<4.0.0',
 'matplotlib>=3.6.0,<4.0.0',
 'pluggy>=1.0.0,<2.0.0',
 'pyroll-core>=2.0.0b,<3.0.0']

entry_points = \
{'pyroll.cli.commands': ['report = pyroll.report.cli:report']}

setup_kwargs = {
    'name': 'pyroll-report',
    'version': '2.0.0b1',
    'description': 'PyRoll rolling simulation framework - HTML report generation.',
    'long_description': '# PyRoll Rolling Simulation Framework\n\nWelcome to The PyRoll Project!\n\nPyRoll is an OpenSource rolling framework, aimed to provide a fast and extensible base for rolling simulation.\nThe current focus lies on groove rolling in elongation grooves.\nThe core package comes with a basic set of models to allow a first estimation of forces and torques occurring in a pass\nsequence.\nThere is a flexible plugin system, able to modify and extend the model set available to describe the process.\n\n## Installation\n\nThe PyRoll Core package is installable via [PyPI](https://pypi.org)\n\n```shell\npip install pyroll\n```\n\nA collection of plugin packages can be installed the same way, the packages names usually start with `pyroll-`.\nUse the [PyPI search](https://pypi.org/search/?q=pyroll) or look at the\nprojects [GitHub page](https://github.com/pyroll-project) for discovering plugins.\n\n## Basic Usage\n\nThe package provides a simple CLI tool that can be used to load input data, run the solution procedure and export the\nsolution data.\nThe CLI provides several commands that can and must be chained in one call.\nNo state is preserved between different program runs.\n\nThe simplest use case is to read from a python script, solve and render the results to an HTML report page.\nThe default input file is `input.py`, the default report file `report.html`.\n\n```shell\npyroll input-py solve report\n```\n\nOne may specify the files explicitly with the `-f`/`--file` option:\n\n```shell\npyroll input-py -f other_input.py solve report -f other_report.html\n```\n\nA most basic input file may look like:\n\n```python\nfrom pyroll.core import Profile, RollPass, Transport, Roll, DiamondGroove, SquareGroove\n\nin_profile = Profile.square(\n    side=45e-3, corner_radius=3e-3,\n    temperature=1200 + 273.15, flow_stress=100e6, strain=0,\n)\n\nsequence = [\n    RollPass(\n        label="Diamond I", velocity=1, gap=3e-3,\n        roll=Roll(\n            groove=DiamondGroove(\n                usable_width=76.5e-3, tip_depth=22e-3, r1=12e-3, r2=8e-3\n            ),\n            nominal_radius=160e-3\n        )\n    ),\n    Transport(duration=2),\n    RollPass(\n        label="Square II", velocity=1, gap=3e-3,\n        roll=Roll(\n            groove=SquareGroove(\n                usable_width=52.7e-3, tip_depth=26e-3, r1=8e-3, r2=6e-3\n            ),\n            nominal_radius=160e-3\n        )\n    ),\n]\n```\n\nThe file must define the variables `in_profile` and `sequence` defining the state of the initial workpiece and the\nsequence of roll passes and transport ranges.\nFor a more advanced example, representing a pass sequence at the 3-high mill at the Institute of Metals Forming, run:\n\n```shell\npyroll create-input-py -k trio -f input.py\n```\n\nThe PyRoll command line interface resides additionally on a YAML configuration file `config.yaml`.\nThe default file can be created using the following command:\n\n```shell\npyroll create-config\n```\n\nThe core section of this file is the `plugins` section.\nHere one can specify a list of plugins that will be loaded in each simulation run.\nAnother way of loading plugins is to directly import them in the input Python script.\n\nIt is recommended to create a fresh directory for each simulation project to avoid the need to specify the filenames explicitly.\nA basic input and config file can be created in the current directory using \n\n```shell\npyroll new\n```\n\nOne may also use the appropriate classes and functions directly from Python code, see\nthe [documentation](https://pyroll.readthedocs.io/en/latest) for more examples.\n\n## Documentation\n\nSee the [documentation](https://pyroll.readthedocs.io/en/latest) to learn about basic concepts and\nusage.\n\n## License\n\nThe project is licensed under the [BSD 3-Clause license](LICENSE).\n\n## Contributing\n\nSince the project is currently in initial state, we would ask you to contact us first if you would like to contribute.\nThis helps to avoid unnecessary effort by you and us. Use the issue system\nor [mail us](mailto:kalibrierzentrum@imf.tu-freiberg.de). If you want to create your own plugin package, please use\nthe [plugin template](https://github.com/pyroll-project/pyroll-plugin-template) and follow the instructions there.\n\n## Roadmap\n\nSee the [roadmap](ROADMAP.md) for information about ongoing development and future plans.',
    'author': 'Max Weiner',
    'author_email': 'max.weiner@imf.tu-freiberg.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://pyroll-project.github.io',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
