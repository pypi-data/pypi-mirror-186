# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['embodycodec']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'embody-codec',
    'version': '1.0.16',
    'description': 'Embody Protocol Codec',
    'long_description': "# EmBody protocol codec\n\n[![PyPI](https://img.shields.io/pypi/v/embody-codec.svg)][pypi_]\n[![Status](https://img.shields.io/pypi/status/embody-codec.svg)][status]\n[![Python Version](https://img.shields.io/pypi/pyversions/embody-codec)][python version]\n[![License](https://img.shields.io/pypi/l/embody-codec)][license]\n\n[![Tests](https://github.com/aidee-health/embody-codec/workflows/Tests/badge.svg)][tests]\n\n[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]\n[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]\n\n[pypi_]: https://pypi.org/project/embody-codec/\n[status]: https://pypi.org/project/embody-codec/\n[python version]: https://pypi.org/project/embody-codec\n[tests]: https://github.com/aidee-health/embody-codec/actions?workflow=Tests\n[pre-commit]: https://github.com/pre-commit/pre-commit\n[black]: https://github.com/psf/black\n\nThis is a Python based implementation library for the Aidee EmBody communication protocol.\n\n## Features\n\n- Encode protocol messages to binary data (bytes)\n- Decode binary data to protocol messages\n- Accessory code\n\n## Requirements\n\n- This library does not require any external libraries\n- Requires Python 3.7+\n\n# Installing package with pip from github\n\nYou can install _embody codec_ via [pip] from [PyPI]:\n\n```console\npip install embody-codec\n```\n\n## Contributing\n\nContributions are very welcome. To learn more, see the [Contributor Guide].\n\n## License\n\nDistributed under the terms of the [MIT license][license].\n\n## Issues\n\nIf you encounter any problems,\nplease [file an issue] along with a detailed description.\n\n## Credits\n\nThis project was generated from [@cjolowicz]'s [Hypermodern Python Cookiecutter] template.\n\n[@cjolowicz]: https://github.com/cjolowicz\n[pypi]: https://pypi.org/\n[hypermodern python cookiecutter]: https://github.com/cjolowicz/cookiecutter-hypermodern-python\n[file an issue]: https://github.com/espenwest/hypermodern-python/issues\n[pip]: https://pip.pypa.io/\n\n<!-- github-only -->\n\n[license]: https://github.com/aidee-health/embody-codec/blob/main/LICENSE\n[contributor guide]: https://github.com/aidee-health/embody-codec/blob/main/CONTRIBUTING.md\n",
    'author': 'Aidee Health AS',
    'author_email': 'hello@aidee.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/aidee-health/embody-protocol-codec',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
