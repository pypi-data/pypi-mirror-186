# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['single_mol']

package_data = \
{'': ['*']}

install_requires = \
['ipykernel>=6.19.4', 'msions>=0.3.1', 'pandas>=1.5.2', 'pymzml>=2.5.2']

setup_kwargs = {
    'name': 'single-mol',
    'version': '0.1.1',
    'description': 'A package to accompany the Single Molecule Counting Perspective.',
    'long_description': '# single_mol\n\nA package to accompany the Single Molecule Counting Perspective.\n\n## Installation\n\n```bash\n$ pip install single_mol\n```\n\n## Usage\n\n`single_mol` can be used to recreate figures from the Single Molecule Counting Perspective.\n\nSee the [documentation](https://single_mol.readthedocs.io/en/latest/example.html) for examples.\n\n## Files\n\nBecause some files are too large for GitHub, the files needed to recreate the figures can be found on [Panorama](https://panoramaweb.org/Single_Molecule_Counting.url).\n\n## Contributing\n\nInterested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.\n\n## License\n\n`single_mol` was created by Danielle A. Faivre. It is licensed under the terms of the Apache License 2.0 license.\n\n## Credits\n\n`single_mol` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).\n',
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
