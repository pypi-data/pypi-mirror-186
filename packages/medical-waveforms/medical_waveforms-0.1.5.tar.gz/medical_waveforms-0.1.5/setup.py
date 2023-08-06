# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['medical_waveforms', 'medical_waveforms.features']

package_data = \
{'': ['*'], 'medical_waveforms': ['data/*']}

install_requires = \
['matplotlib>=3.5.1,<4.0.0',
 'numpy>=1.22,<2.0',
 'pandas>=1.3.4,<2.0.0',
 'pyampd>=0.0.1,<0.0.2',
 'pydantic>=1.9.2,<2.0.0',
 'scipy>=1.7.3,<2.0.0']

setup_kwargs = {
    'name': 'medical-waveforms',
    'version': '0.1.5',
    'description': 'Preprocessing and analysis of physiological waveforms',
    'long_description': '![Run tests workflow](https://github.com/UCL-Chimera/medical-waveforms/actions/workflows/run_tests.yml/badge.svg) ![Linting workflow](https://github.com/UCL-Chimera/medical-waveforms/actions/workflows/lint.yml/badge.svg)\n\n# medical-waveforms\n\n**medical-waveforms** is a Python package for preprocessing and analysis of physiological waveforms.\n\nThis package currently focuses on:\n\n- Splitting waveforms into individual cycles (e.g. splitting a respiratory waveform into individual breaths)\n- Extracting features from individual cycles\n- Rule-based signal quality assessment\n\n\n## Installation\n\nInstall with:\n\n```\npip install medical-waveforms\n```\n\nThe package is tested on Python 3.8 - 3.11.\n\n\n## Getting started\n\nSee the [tutorial notebook](https://github.com/UCL-Chimera/medical-waveforms/blob/main/examples/tutorial.ipynb) for a general introduction to using the package.\n\nThe [signal quality assessment notebook](https://github.com/UCL-Chimera/medical-waveforms/blob/main/examples/signal_quality.ipynb) demonstrates customisation of the signal quality assessment process.\n\nThese tutorials currently focus on arterial blood pressure waveforms, but can be adapted to other physiological waveforms.\n\n\n## Contributing to this project\n\nContributions are very welcome! Please see [CONTRIBUTING.md](https://github.com/UCL-Chimera/medical-waveforms/blob/main/CONTRIBUTING.md) to get started.\n\n\n## Acknowledgements\n\nOur signal quality assessment pipeline is adapted from that used in the excellent [PhysioNet Cardiovascular Signal Toolbox](https://github.com/cliffordlab/PhysioNet-Cardiovascular-Signal-Toolbox). Many thanks to its [contributors](https://github.com/cliffordlab/PhysioNet-Cardiovascular-Signal-Toolbox/graphs/contributors).\n',
    'author': 'Finneas Catling',
    'author_email': 'f.catling@imperial.ac.uk',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/UCL-Chimera/medical-waveforms',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8',
}


setup(**setup_kwargs)
