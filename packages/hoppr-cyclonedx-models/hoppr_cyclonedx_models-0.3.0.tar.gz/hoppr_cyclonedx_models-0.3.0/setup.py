# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hoppr_cyclonedx_models',
 'hoppr_cyclonedx_models.cyclonedx_1_3',
 'hoppr_cyclonedx_models.cyclonedx_1_4']

package_data = \
{'': ['*']}

install_requires = \
['pydantic[email]>=1.10.2,<2.0.0']

setup_kwargs = {
    'name': 'hoppr-cyclonedx-models',
    'version': '0.3.0',
    'description': 'CycloneDX Pydantic models for easy use in your Python project.',
    'long_description': "# hoppr_cyclonedx_models\n\n[![pypi](https://img.shields.io/pypi/v/hoppr-cyclonedx-models)](https://pypi.org/project/hoppr-cyclonedx-models)\n[![downloads](https://pepy.tech/badge/hoppr-cyclonedx-models/month)](https://pepy.tech/project/hoppr-cyclonedx-models)\n[![versions](https://img.shields.io/badge/python-3.7.2-blue.svg)](https://gitlab.com/hoppr/hoppr-cyclonedx-models)\n[![license](https://img.shields.io/gitlab/license/hoppr/hoppr-cyclonedx-models)](https://gitlab.com/hoppr/hoppr-cyclonedx-models/-/blob/main/LICENSE)\n\nSerializable CycloneDX Models.   Quickly get up and running with models generated directly off the specification.\n\nCurrent generated models can be found here: [Generated Models](https://gitlab.com/hoppr/hoppr-cyclonedx-models/-/tree/main/hoppr_cyclonedx_models)\n\n## Installation\n\nInstall using `pip install -U hoppr-cyclonedx-models` or `poetry add hoppr-cyclonedx-models`.  \n\n## A Simple Example:\n\n```py\nfrom hoppr_cyclonedx_models.cyclonedx_1_4 import Component\n\ndata = {'type': 'library', 'purl': 'pkg:pypi/django@1.11.1', 'name': 'django', 'version': '1.11.1'}\n\ncomponent = Component(**data)\nprint(component.purl)\n```\n\n## Contributing\n\nFor guidance setting up a development environment and how to make a contribution to _hoppr-cyclonedx-models_, see [Contributing to Hoppr](https://hoppr.dev/docs/development/contributing).\n",
    'author': 'LMCO Open Source',
    'author_email': 'open.source@lmco.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://gitlab.com/hoppr/hoppr-cyclonedx-models',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.2,<4.0.0',
}


setup(**setup_kwargs)
