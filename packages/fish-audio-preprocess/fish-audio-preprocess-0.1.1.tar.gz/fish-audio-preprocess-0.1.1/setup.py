# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fish_audio_preprocess',
 'fish_audio_preprocess.cli',
 'fish_audio_preprocess.cli.so_vits_svc',
 'fish_audio_preprocess.utils']

package_data = \
{'': ['*']}

install_requires = \
['PySoundFile>=0.9.0,<0.10.0',
 'black>=22.12.0,<23.0.0',
 'demucs>=4.0.0,<5.0.0',
 'librosa>=0.9.0,<0.10.0',
 'llvmlite>=0.39.1,<0.40.0',
 'loguru>=0.6.0,<0.7.0',
 'matplotlib>=3.6.2,<4.0.0',
 'numba>=0.56.4,<0.57.0',
 'praat-parselmouth>=0.4.3,<0.5.0',
 'pyloudnorm>=0.1.1,<0.2.0',
 'tqdm>=4.64.1,<5.0.0',
 'transformers>=4.25.1,<5.0.0']

extras_require = \
{'so-vits-svc': ['pyworld>=0.3.2,<0.4.0']}

entry_points = \
{'console_scripts': ['fap = fish_audio_preprocess.cli.__main__:cli']}

setup_kwargs = {
    'name': 'fish-audio-preprocess',
    'version': '0.1.1',
    'description': 'Preprocess audio data',
    'long_description': None,
    'author': 'Lengyue',
    'author_email': 'lengyue@lengyue.me',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
