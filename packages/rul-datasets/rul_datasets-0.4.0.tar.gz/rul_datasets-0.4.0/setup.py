# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rul_datasets', 'rul_datasets.reader']

package_data = \
{'': ['*']}

install_requires = \
['pytorch-lightning>=1.4.4,<2.0.0',
 'scikit-learn>=1.0.0,<2.0.0',
 'torch>=1.9.0,<2.0.0',
 'tqdm>=4.62.2,<5.0.0']

setup_kwargs = {
    'name': 'rul-datasets',
    'version': '0.4.0',
    'description': 'A collection of datasets for RUL estimation as Lightning Data Modules.',
    'long_description': '# RUL Datasets\n\n[![Master](https://github.com/tilman151/rul-datasets/actions/workflows/on_push.yaml/badge.svg)](https://github.com/tilman151/rul-datasets/actions/workflows/on_push.yaml)\n[![Release](https://github.com/tilman151/rul-datasets/actions/workflows/on_release.yaml/badge.svg)](https://github.com/tilman151/rul-datasets/actions/workflows/on_release.yaml)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n\nThis library contains a collection of common benchmark datasets for **remaining useful lifetime (RUL)** estimation.\nThey are provided as [LightningDataModules](https://pytorch-lightning.readthedocs.io/en/stable/api/pytorch_lightning.core.LightningDataModule.html#pytorch_lightning.core.LightningDataModule) to be readily used in [PyTorch Lightning](https://pytorch-lightning.readthedocs.io/en/latest/).\n\nCurrently, four datasets are supported:\n\n* **C-MAPSS** Turbofan Degradation Dataset\n* **FEMTO** (PRONOSTIA) Bearing Dataset\n* **XJTU-SY** Bearing Dataset\n* **Dummy** A tiny, simple dataset for debugging\n\nAll datasets share the same API, so they can be used as drop-in replacements for each other.\nThat means, if an experiment can be run with one of the datasets, it can be run with all of them.\nNo code changes needed.\n\nAside from the basic ones, this library contains data modules for advanced experiments concerning **transfer learning**, **unsupervised domain adaption** and **semi-supervised learning**.\nThese data modules are designed as **higher-order data modules**.\nThis means they take one or more of the basic data modules as inputs and adjust them to the desired use case.\n\n## Installation\n\nThe library is pip-installable. Simply type:\n\n```shell\npip install rul-datasets\n```\n\n## Contribution\n\nContributions are always welcome. Whether you want to fix a bug, add a feature or a new dataset, just open an issue and a PR.',
    'author': 'Krokotsch, Tilman',
    'author_email': 'tilman.krokotsch@tu-berlin.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://krokotsch.eu/rul-datasets',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
