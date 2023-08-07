# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['paule']

package_data = \
{'': ['*'], 'paule': ['vocaltractlab_api/*']}

install_requires = \
['librosa>=0.9.2,<0.10.0',
 'llvmlite>=0.39.1,<0.40.0',
 'numba>=0.56.4,<0.57.0',
 'numpy>=1.23.1,<2.0.0',
 'pandas>=1.4.3,<2.0.0',
 'soundfile>=0.11.0,<0.12.0',
 'toml>=0.10.2,<0.11.0',
 'torch>=1.13.1,<2.0.0',
 'tqdm>=4.64.1,<5.0.0']

setup_kwargs = {
    'name': 'paule',
    'version': '0.3.4',
    'description': 'paule implements the Predictive Articulatory speech synthesis model Utilizing Lexical Embeddings (PAULE), which is a control model for the articulatory speech synthesizer VocalTractLab (VTL).',
    'long_description': 'PAULE\n=====\n\n.. image:: https://zenodo.org/badge/355606517.svg\n   :target: https://zenodo.org/badge/latestdoi/355606517\n\nPredictive Articulatory speech synthesis Utilizing Lexical Embeddings (PAULE) a\npython frame work to plan control parameter trajectories for the VocalTractLab\nsimulator for a target acoustics or semantic embedding.\n\nAcknowledgements\n----------------\nThis research was supported by an ERC advanced Grant (no. 742545) and the University of Tübingen.\n',
    'author': 'Konstantin Sering',
    'author_email': 'konstantin.sering@uni-tuebingen.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://paule.readthedocs.io/en/latest/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.12',
}


setup(**setup_kwargs)
