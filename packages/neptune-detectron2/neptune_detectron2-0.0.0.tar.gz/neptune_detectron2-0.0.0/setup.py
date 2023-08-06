# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['neptune_detectron2', 'neptune_detectron2.impl']

package_data = \
{'': ['*']}

install_requires = \
['fvcore<0.1.5.post20221220',
 'neptune-client>=0.10.0',
 'numpy<1.24.0',
 'torch>=1.13.0,<2.0.0',
 'torchvision>=0.14.0,<0.15.0']

extras_require = \
{':python_version < "3.8"': ['importlib-metadata'],
 'dev': ['pre-commit', 'pytest>=5.0', 'pytest-cov==2.10.1']}

setup_kwargs = {
    'name': 'neptune-detectron2',
    'version': '0.0.0',
    'description': 'Neptune.ai detectron2 integration library',
    'long_description': '# Neptune - detectron2 integration\n\nSee [the official docs](https://docs.neptune.ai/integrations-and-supported-tools/model-training/).\n',
    'author': 'neptune.ai',
    'author_email': 'contact@neptune.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://neptune.ai/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
