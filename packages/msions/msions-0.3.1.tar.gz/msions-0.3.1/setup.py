# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['msions']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.5,<3.6', 'pandas>=1.5.2', 'pymzml>=2.5.2', 'seaborn>=0.12.1']

setup_kwargs = {
    'name': 'msions',
    'version': '0.3.1',
    'description': 'A python package for creating MS TIC and ion plots',
    'long_description': "# msions\n\n'A python package for creating MS TIC and ion plots'\n\n## Installation\n\n```bash\n$ pip install msions\n```\n\n## Usage\n`msions` can be used to work with Hardklor and Kronik files and to create MS TIC and ion plots.\n\n```python\nimport msions.mzml as mzml\nimport msions.hardklor as hk\nimport msions.kronik as kro\nimport msions.percolator as perc\nimport msions.encyclopedia as encyclo\nimport msions.msplot as msplot\nimport msions.utils as msutils\n```\n\nSee the [documentation](https://msions.readthedocs.io/en/latest/example.html) for examples.\n\n## Contributing\n\nInterested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.\n\n## License\n\n`msions` was created by Danielle A. Faivre. It is licensed under the terms of the Apache License 2.0 license.\n\n## Credits\n\n`msions` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).\n",
    'author': 'Danielle A. Faivre',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9',
}


setup(**setup_kwargs)
