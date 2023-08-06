# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hygia',
 'hygia.data_pipeline',
 'hygia.data_pipeline.feature_engineering',
 'hygia.data_pipeline.model',
 'hygia.data_pipeline.pre_process_data',
 'hygia.parser']

package_data = \
{'': ['*']}

install_requires = \
['altair==4.2.0',
 'attrs==22.2.0',
 'bpemb==0.3.4',
 'certifi==2022.12.7',
 'charset-normalizer==3.0.1',
 'contourpy==1.0.6',
 'coverage==7.0.2',
 'cycler==0.11.0',
 'entrypoints==0.4',
 'exceptiongroup==1.1.0',
 'fonttools==4.38.0',
 'gensim==3.8.3',
 'idna==3.4',
 'importlib-resources==5.10.2',
 'iniconfig==1.1.1',
 'jinja2==3.1.2',
 'joblib==1.2.0',
 'jsonschema==4.17.3',
 'kiwisolver==1.4.4',
 'markupsafe==2.1.1',
 'matplotlib==3.6.2',
 'numpy==1.24.1',
 'packaging==23.0',
 'pandas==1.5.2',
 'pillow==9.4.0',
 'pkgutil-resolve-name==1.3.10',
 'pluggy==1.0.0',
 'pyparsing==3.0.9',
 'pyrsistent==0.19.3',
 'pytest-cov==4.0.0',
 'pytest==7.2.0',
 'python-dateutil==2.8.2',
 'pytz==2022.7',
 'pyyaml==6.0',
 'requests==2.28.2',
 'scikit-learn==1.2.0',
 'scipy==1.9.3',
 'sentencepiece==0.1.97',
 'six==1.16.0',
 'smart-open==6.3.0',
 'threadpoolctl==3.1.0',
 'tomli==2.0.1',
 'toolz==0.12.0',
 'tqdm==4.64.1',
 'urllib3==1.26.14',
 'whatlies==0.7.0',
 'wheel==0.38.4',
 'zipp==3.11.0']

setup_kwargs = {
    'name': 'hygia',
    'version': '0.1.9',
    'description': 'A short description of the package.',
    'long_description': '<p align="center">\n    <img src="./assets/img/horizontal_logo.PNG" alt="hygia-logo" style="width:500px;"/>\n</p>\n\n# A powerful Python ML playground toolkit\n\n[![PyPI Latest Release](https://img.shields.io/pypi/v/hygia.svg)](https://pypi.org/project/hygia/)\n[![License](https://img.shields.io/pypi/l/hygia.svg)](https://github.com/hygia-org/hygia/blob/main/LICENSE)\n[![Coverage](https://codecov.io/github/hygia-org/hygia/coverage.svg?branch=main)](https://codecov.io/gh/hygia-org/hygia)\n\n<!-- [![Package Status](https://img.shields.io/pypi/status/hygia.svg)](https://pypi.org/project/hygia/) -->\n\n## What is it?\n\nHygia is a Python package that provides fast, flexible, and expressive data pipeline configuration through a YAML file to make working with Machine Learning data easy and intuitive. It consists of helping developers and users to register, organize, compare and share all their ML model metadata in a single place, facilitating the generation of requirements in the ETL (Extract, Transform and Load) process. Thus, the migration can be scaled, automated, and accelerated for similar contexts.\n\n## Main Features\n\n- Configure data pipeline through a YAML file\n- Execute through command line or python import\n- Pack the solution into a Python\'s Package Manager\n- Visualize results in customized dashboards\n- Test on different databases\n\n## Where to get it\n\nThe source code is currently hosted on GitHub at: `https://github.com/hygia-org`\n\n## Installation from sources\n\n```\npython -m venv env\nsource env/bin/activate\npip install -r requirements.txt\n```\n\n### Boilerplate\n\n```\nexamples/hygia_boilerplate.ipynb\n```\n\n### Testing\n\n```\npytest --cov\n```\n\n### Documentation\n\nWe used sphinx to write the documentation\n\nTo run locally, you need to install sphinx:\n\n```\npip install sphinx\n```\n\nThen install the theme used:\n\n```\npip install pydata-sphinx-theme\n```\n\nAnd Run the project\n\n```\nsphinx-build -b html source ./\n```\n\nAnd open the index.html\n',
    'author': 'PDA-FGA',
    'author_email': 'rocha.carla@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/PDA-FGA/Playground',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
