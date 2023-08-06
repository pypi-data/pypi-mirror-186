# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sketch_converter']

package_data = \
{'': ['*']}

install_requires = \
['colorama>=0.4.6,<0.5.0',
 'commonmark>=0.9.1,<0.10.0',
 'numpy>=1.24.1,<2.0.0',
 'opencv-python>=4.7.0.68,<5.0.0.0',
 'pygments>=2.14.0,<3.0.0',
 'rich>=13.0.0,<14.0.0',
 'shellingham>=1.5.0.post1,<2.0.0',
 'typer>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['sketch-converter = sketch_converter.cli:app']}

setup_kwargs = {
    'name': 'sketch-converter',
    'version': '0.1.1',
    'description': 'Converter your picture into sketch with just one line of command',
    'long_description': '<p align="center">\n  <img style="width:40%;" src="logo/sketch.png" />\n</p>\n\n<h1 align="center">Image to Sketch Converter</h1>\n\n<h3 align="center">Fond of **sketches**, but bad at **art**? 🥴</h3>\n<br>\n\n[![main-ci](https://github.com/samyak-jn/sketch-converter/actions/workflows/main.yml/badge.svg)](https://github.com/samyak-jn/sketch-converter/actions/workflows/main.yml)\n[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/samyak-jn/sketch-converter/master.svg)](https://results.pre-commit.ci/latest/github/samyak-jn/sketch-converter/master)\n![PyPI](https://img.shields.io/pypi/v/sketch-converter)\n![PyPI - Format](https://img.shields.io/pypi/format/sketch-converter)\n![PyPI - Status](https://img.shields.io/pypi/status/sketch-converter?color=orange)\n![PyPI - Implementation](https://img.shields.io/pypi/implementation/sketch-converter)\n![PyPI - Wheel](https://img.shields.io/pypi/wheel/sketch-converter)\n\n<a href="https://github.com/python/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>\n<a href="https://github.com/samyak-jn/sketch-converter/blob/master/LICENSE"><img alt="License: MIT" src="https://black.readthedocs.io/en/stable/_static/license.svg"></a>\n<img src="https://img.shields.io/badge/made%20with-python-blue.svg" alt="made with python">\n\n\nHere\'s a little something for people like you and me.\nThis is a simple python script that converts your **captured images** into a **sketch** in real-time with just one line of command, fascinating? 😎\n\nThis script is written with the help of the OpenCV library in python.All the sketches will be saved in the parent directory itself.\n\n### Quick Setup\n\n```bash\n# Clone the repository\ngit clone https://github.com/samyak-jn/sketch-converter.git\npoetry shell\npoetry install\nsketch_converter --help\n```\n\n## Camera Usage\n\n```bash\n# video_src = 1 , grayscale mode = 1\nsketch_converter video-capture 1 1\n```\n\n### Contributing ✔️\n\n- Please contribute using [Github Flow](https://guides.github.com/introduction/flow/). Create a branch, add commits, and [open a pull request](https://github.com/fraction/readme-boilerplate/compare/).\n\n- All the issues/features are welcome. Open a PR and let\'s have a discussion.\n\n### License\nsketch-converter is licensed under [MIT](https://github.com/samyak-jn/sketch-converter/blob/master/LICENSE), hence it is open source for all.\n\n---\nCopyright © 2023 Onuralp SEZER, Samyak Jain\n',
    'author': 'Onuralp SEZER',
    'author_email': 'thunderbirdtr@fedoraproject.org',
    'maintainer': 'Samyak Jain',
    'maintainer_email': 'samyak.jn11@gmail.com',
    'url': 'https://github.com/samyak-jn/sketch-converter',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
