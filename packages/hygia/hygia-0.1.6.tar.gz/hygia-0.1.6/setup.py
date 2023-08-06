# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hygia']

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
 'zipp==3.11.0']

setup_kwargs = {
    'name': 'hygia',
    'version': '0.1.6',
    'description': 'A short description of the package.',
    'long_description': '# Playground\n\n### Instaling Requirements\n\n```\npython -m venv env\nsource env/bin/activate\npip install -r requirements.txt\n```\n\n### Running\n\n```\npython src/main.py\n```\n\n### Testing\n\n```\npytest --cov\n```\n\n### Metabase\n\nThe metabase will help us visualize and monitor data processing, feature engineering and model monitoring, accompanying us throughout the cycle.\n\n| Keywords  | Description |\n|-----------|-------------|\n|   CSV     | A CSV file is a plain text file that stores table and spreadsheet information. CSV files can be easily imported and exported using programs that store data in tables.|\n| Collection| A collection is a grouping of MongoDB documents. Documents within a collection can have different fields. A collection is the equivalent of a table in a relational database system.|\n|  Database | A database stores one or more collections of documents.|\n| Mongo| It is a NoSQL database developed by MongoDB Inc. MongoDB database is built to store a huge amount of data and also perform fast.|\n\n**Environment check**\n\nCheck if docker exists, if not then [install it](https://docs.docker.com/engine/install/ubuntu/) \n```docker -v ```\n\nCheck if docker-compose exists, if not then [install it](https://docs.docker.com/compose/install/) \n```docker-compose -v ```\n\nwhen running the first time create the network \n\n```make network```\n\n**Run metabase local**\n\nIn the root folder, run the command\n\n```make up```\n\n**Loading data into a non-relational database**\n\nThis command is used to load the .csv file into the local database, where it is necessary to pass the file path, database and collection as an argument\n\n- path = .csv file path\n- database = database name\n- collection = collection name\n\nexemple:\n\n\n```make migrate path=data/data_example.csv database=general  collection=order```\n\n\n\n**Connect the database to the metabase**\n\n- step 1: Open localhost:3000\n- step 2: Click Admin setting\n- step 3: Click Database\n- step 4: Add database authentication data\n\n![](https://raw.githubusercontent.com/francisco1code/Files/main/a.gif)\n\n**Exemple mongo connect metabase**\n|  metabase  | credential  |\n|------------|-------------|\n|    host    |  mongo  |\n|dabase_name | use the name you define in make migrate|\n|    user    |   lappis    |\n|  password  |   lappis    |\n\n\n### Documentation\n\nWe used sphinx to write the documentation\n\nTo run locally, you need to install sphinx:\n\n```pip install sphinx```\n\nThen install the theme used:\n\n```pip install pydata-sphinx-theme```\n\nAnd Run the project\n\n```sphinx-build -b html source ./``` \n\nAnd open the index.html',
    'author': 'PDA-FGA',
    'author_email': 'rocha.carla@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/PDA-FGA/Playground',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
