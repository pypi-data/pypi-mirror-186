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
{'': ['*'], 'hygia': ['yamls/*']}

install_requires = \
['altair==4.2.0',
 'attrs==22.2.0',
 'bpemb==0.3.4',
 'certifi==2022.12.7',
 'charset-normalizer==2.1.1',
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
 'packaging==22.0',
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
 'requests==2.28.1',
 'scikit-learn==1.2.0',
 'scipy==1.9.3',
 'sentencepiece==0.1.97',
 'six==1.16.0',
 'smart-open==6.3.0',
 'threadpoolctl==3.1.0',
 'tomli==2.0.1',
 'toolz==0.12.0',
 'tqdm==4.64.1',
 'urllib3==1.26.13',
 'whatlies==0.7.0',
 'zipp==3.11.0']

setup_kwargs = {
    'name': 'hygia',
    'version': '0.1.0',
    'description': 'A short description of the package.',
    'long_description': '# Playground\n\n### Instaling Requirements\n\n```\npython -m venv env\nsource env/bin/activate\npip install -r requirements.txt\n```\n\n### Running\n\n```\npython src/main.py\n```\n\n### Testing\n\n```\npytest --cov\n```\n',
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
