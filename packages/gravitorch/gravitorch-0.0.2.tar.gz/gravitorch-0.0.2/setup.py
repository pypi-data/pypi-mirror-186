# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['gravitorch',
 'gravitorch.cli',
 'gravitorch.creators',
 'gravitorch.creators.core',
 'gravitorch.creators.dataloader',
 'gravitorch.creators.datapipe',
 'gravitorch.creators.datasource',
 'gravitorch.creators.lr_scheduler',
 'gravitorch.creators.model',
 'gravitorch.creators.optimizer',
 'gravitorch.data',
 'gravitorch.data.datacreators',
 'gravitorch.data.dataloaders',
 'gravitorch.data.dataloaders.collators',
 'gravitorch.data.datapipes',
 'gravitorch.data.datapipes.iter',
 'gravitorch.data.datasets',
 'gravitorch.data.partitioners',
 'gravitorch.datasources',
 'gravitorch.distributed',
 'gravitorch.engines',
 'gravitorch.experimental',
 'gravitorch.handlers',
 'gravitorch.lr_schedulers',
 'gravitorch.models',
 'gravitorch.models.criterions',
 'gravitorch.models.metrics',
 'gravitorch.models.metrics.classification',
 'gravitorch.models.metrics.regression',
 'gravitorch.models.networks',
 'gravitorch.models.utils',
 'gravitorch.nn',
 'gravitorch.nn.experimental',
 'gravitorch.nn.functional',
 'gravitorch.nn.functional.experimental',
 'gravitorch.nn.fusion',
 'gravitorch.nn.utils',
 'gravitorch.optimizers',
 'gravitorch.runners',
 'gravitorch.utils',
 'gravitorch.utils.artifacts',
 'gravitorch.utils.data_summary',
 'gravitorch.utils.device_placement',
 'gravitorch.utils.engine_states',
 'gravitorch.utils.evaluation_loops',
 'gravitorch.utils.events',
 'gravitorch.utils.exp_trackers',
 'gravitorch.utils.history',
 'gravitorch.utils.loop_observers',
 'gravitorch.utils.meters',
 'gravitorch.utils.parameter_initializers',
 'gravitorch.utils.profilers',
 'gravitorch.utils.tensor',
 'gravitorch.utils.training_loops']

package_data = \
{'': ['*']}

install_requires = \
['coola>=0.0,<0.1',
 'hya>=0.0,<0.1',
 'hydra-core>=1.3,<2.0',
 'numpy>=1.23,<2.0',
 'objectory>=0.0,<0.1',
 'pytorch-ignite>=0.4,<0.5',
 'tabulate>=0.9,<0.10',
 'torch>=1.13,<2.0',
 'tqdm>=4.64,<5.0']

extras_require = \
{'all': ['accelerate>=0.15,<0.16',
         'colorlog>=6.7,<7.0',
         'matplotlib>=3.6,<4.0',
         'pillow>=9.3,<10.0',
         'tensorboard>=2.11,<3.0',
         'torchvision>=0.14,<0.15'],
 'tb': ['tensorboard>=2.11,<3.0'],
 'vision': ['pillow>=9.3,<10.0', 'torchvision>=0.14,<0.15']}

setup_kwargs = {
    'name': 'gravitorch',
    'version': '0.0.2',
    'description': 'Warning: API is not stable',
    'long_description': '\n[//]: # (<p align="center">)\n\n[//]: # (   <a href="https://github.com/durandtibo/meteor/actions">)\n\n[//]: # (      <img alt="CI" src="https://github.com/durandtibo/meteor/workflows/CI/badge.svg?event=push&branch=main">)\n\n[//]: # (   </a>)\n\n[//]: # (    <a href="https://pypi.org/project/gravitorch/">)\n\n[//]: # (      <img alt="PYPI version" src="https://img.shields.io/pypi/v/gravitorch">)\n\n[//]: # (    </a>)\n\n[//]: # (   <a href="https://pypi.org/project/gravitorch/">)\n\n[//]: # (      <img alt="Python" src="https://img.shields.io/pypi/pyversions/gravitorch.svg">)\n\n[//]: # (   </a>)\n\n[//]: # (   <a href="https://opensource.org/licenses/BSD-3-Clause">)\n\n[//]: # (      <img alt="BSD-3-Clause" src="https://img.shields.io/pypi/l/gravitorch">)\n\n[//]: # (   </a>)\n\n[//]: # (   <a href="https://codecov.io/gh/durandtibo/meteor">)\n\n[//]: # (      <img alt="Codecov" src="https://codecov.io/gh/durandtibo/meteor/branch/main/graph/badge.svg">)\n\n[//]: # (   </a>)\n\n[//]: # (   <a href="https://github.com/psf/black">)\n\n[//]: # (     <img  alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg">)\n\n[//]: # (   </a>)\n\n[//]: # (   <a href="https://google.github.io/styleguide/pyguide.html#s3.8-comments-and-docstrings">)\n\n[//]: # (     <img  alt="Doc style: google" src="https://img.shields.io/badge/%20style-google-3666d6.svg">)\n\n[//]: # (   </a>)\n\n[//]: # (   <br/>)\n\n[//]: # (</p>)\n\n\n<p align="center">\n   <a>\n      <img alt="CI" src="https://github.com/durandtibo/meteor/workflows/CI/badge.svg?event=push&branch=main">\n   </a>\n    <a href="https://pypi.org/project/gravitorch/">\n      <img alt="PYPI version" src="https://img.shields.io/pypi/v/gravitorch">\n    </a>\n   <a href="https://pypi.org/project/gravitorch/">\n      <img alt="Python" src="https://img.shields.io/pypi/pyversions/gravitorch.svg">\n   </a>\n   <a href="https://opensource.org/licenses/BSD-3-Clause">\n      <img alt="BSD-3-Clause" src="https://img.shields.io/pypi/l/gravitorch">\n   </a>\n   <a>\n      <img alt="Codecov" src="https://codecov.io/gh/durandtibo/meteor/branch/main/graph/badge.svg">\n   </a>\n   <a href="https://github.com/psf/black">\n     <img  alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg">\n   </a>\n   <a href="https://google.github.io/styleguide/pyguide.html#s3.8-comments-and-docstrings">\n     <img  alt="Doc style: google" src="https://img.shields.io/badge/%20style-google-3666d6.svg">\n   </a>\n   <br/>\n</p>\n',
    'author': 'Thibaut Durand',
    'author_email': 'durand.tibo+gh@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
