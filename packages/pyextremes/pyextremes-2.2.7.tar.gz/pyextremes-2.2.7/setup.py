# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pyextremes',
 'pyextremes.extremes',
 'pyextremes.models',
 'pyextremes.multivariate',
 'pyextremes.plotting',
 'pyextremes.tests',
 'pyextremes.tuning']

package_data = \
{'': ['*']}

install_requires = \
['emcee>=3.0.3,<4.0.0',
 'matplotlib>=3.3.0,<4.0.0',
 'numpy>=1.19.0,<2.0.0',
 'pandas>=1.0.0,<2.0.0',
 'scipy>=1.5.0,<2.0.0']

extras_require = \
{'full': ['tqdm>=4.0.0,<5.0.0']}

setup_kwargs = {
    'name': 'pyextremes',
    'version': '2.2.7',
    'description': 'Extreme Value Analysis (EVA) in Python',
    'long_description': '<p align="center" style="font-size:40px; margin:0px 10px 0px 10px">\n    <em>pyextremes</em>\n</p>\n<p align="center">\n    <em>Extreme Value Analysis (EVA) in Python</em>\n</p>\n<p align="center">\n<a href="https://github.com/georgebv/pyextremes/actions/workflows/test.yml" target="_blank">\n    <img src="https://github.com/georgebv/pyextremes/actions/workflows/test.yml/badge.svg" alt="Test">\n</a>\n<a href="https://codecov.io/gh/georgebv/pyextremes" target="_blank">\n    <img src="https://codecov.io/gh/georgebv/pyextremes/branch/master/graph/badge.svg" alt="Coverage">\n</a>\n<a href="https://pypi.org/project/pyextremes" target="_blank">\n    <img src="https://badge.fury.io/py/pyextremes.svg" alt="PyPI Package">\n</a>\n<a href="https://anaconda.org/conda-forge/pyextremes" target="_blank">\n    <img src="https://img.shields.io/conda/vn/conda-forge/pyextremes.svg" alt="Anaconda Package">\n</a>\n</p>\n\n# About\n\n**Documentation:** https://georgebv.github.io/pyextremes/\n\n**License:** [MIT](https://opensource.org/licenses/MIT)\n\n**Support:** [ask a question](https://github.com/georgebv/pyextremes/discussions)\nor [create an issue](https://github.com/georgebv/pyextremes/issues/new/choose),\nany input is appreciated and would help develop the project\n\n**pyextremes** is a Python library aimed at performing univariate\n[Extreme Value Analysis (EVA)](https://en.wikipedia.org/wiki/Extreme_value_theory).\nIt provides tools necessary to perform a wide range of tasks required to\nperform EVA, such as:\n\n- extraction of extreme events from time series using methods such as\nBlock Maxima (BM) or Peaks Over Threshold (POT)\n- fitting continuous distributions, such as GEVD, GPD, or user-specified\ncontinous distributions to the extracted extreme events\n- visualization of model inputs, results, and goodness-of-fit statistics\n- estimation of extreme events of given probability or return period\n(e.g. 100-year event) and of corresponding confidence intervals\n- tools assisting with model selection and tuning, such as selection of\nblock size in BM and threshold in POT\n\nCheck out [this repository](https://github.com/georgebv/pyextremes-notebooks)\nwith Jupyter notebooks used to produce figures for this readme\nand for the official documentation.\n\n# Installation\n\nGet latest version from PyPI:\n\n```shell\npip install pyextremes\n```\n\nInstall with optional dependencies:\n\n```shell\npip install pyextremes[full]\n```\n\nGet latest experimental build from GitHub:\n\n```shell\npip install "git+https://github.com/georgebv/pyextremes.git#egg=pyextremes"\n```\n\nGet pyextremes for the Anaconda Python distribution:\n\n```shell\nconda install -c conda-forge pyextremes\n```\n\n# Illustrations\n\n<p align="center" style="font-size:20px; margin:10px 10px 0px 10px">\n    <em>Model diagnostic</em>\n</p>\n<p align="center" style="font-size:20px; margin:10px 10px 40px 10px">\n  <img src="https://raw.githubusercontent.com/georgebv/pyextremes-notebooks/master/notebooks/documentation/readme%20figures/diagnostic.png" alt="Diagnostic plot" width="600px">\n</p>\n\n<p align="center" style="font-size:20px; margin:10px 10px 0px 10px">\n    <em>Extreme value extraction</em>\n</p>\n<p align="center" style="font-size:20px; margin:10px 10px 40px 10px">\n  <img src="https://raw.githubusercontent.com/georgebv/pyextremes-notebooks/master/notebooks/documentation/readme%20figures/extremes.png" alt="Diagnostic plot" width="600px">\n</p>\n\n<p align="center" style="font-size:20px; margin:10px 10px 0px 10px">\n    <em>Trace plot</em>\n</p>\n<p align="center" style="font-size:20px; margin:10px 10px 40px 10px">\n  <img src="https://raw.githubusercontent.com/georgebv/pyextremes-notebooks/master/notebooks/documentation/readme%20figures/trace.png" alt="Diagnostic plot" width="600px">\n</p>\n\n<p align="center" style="font-size:20px; margin:10px 10px 0px 10px">\n    <em>Corner plot</em>\n</p>\n<p align="center" style="font-size:20px; margin:10px 10px 40px 10px">\n  <img src="https://raw.githubusercontent.com/georgebv/pyextremes-notebooks/master/notebooks/documentation/readme%20figures/corner.png" alt="Diagnostic plot" width="600px">\n</p>\n\n# Acknowledgements\nI wanted to give kudos to [Jean Toilliez](https://github.com/jtoilliez) who has inspired me to develop this open-source project and who taught me a lot about the extreme value theory. Also big thanks to Max Larson who has introduced me to software development and statistics.\n',
    'author': 'George Bocharov',
    'author_email': 'bocharovgeorgii@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://georgebv.github.io/pyextremes',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
