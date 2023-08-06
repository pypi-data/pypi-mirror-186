# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['django_postgresql_dag']

package_data = \
{'': ['*']}

install_requires = \
['django>=3.2', 'psycopg2-binary>=2.9,<3.0']

setup_kwargs = {
    'name': 'django-postgresql-dag',
    'version': '0.4.0',
    'description': 'Directed Acyclic Graph implementation for Django & Postgresql',
    'long_description': "[![codecov](https://codecov.io/gh/OmenApps/django-postgresql-dag/branch/master/graph/badge.svg?token=IJRBEE6R0C)](https://codecov.io/gh/OmenApps/django-postgresql-dag) ![PyPI](https://img.shields.io/pypi/v/django-postgresql-dag?color=green) ![last commit](https://badgen.net/github/last-commit/OmenApps/django-postgresql-dag/main) [![Documentation Status](https://readthedocs.org/projects/django-postgresql-dag/badge/?version=latest)](http://django-postgresql-dag.readthedocs.io/) [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)\n\n# Django & Postgresql-based Directed Acyclic Graphs\n\nThe main distinguishing factor for this project is that it can retrieve entire sections of a graph with far\nfewer queries than most other packages. The trade off is portability: it uses Postgres' Common Table\nExpressions (CTE) to achieve this and is therefore not compatible with other databases.\n\nNOTE: Not all methods which would benefit from CTEs use them yet. **This project is a work in progress. Again, this project is a work in progress.** While functional, it is not yet fully optimized.\n\nThe primary purpose of this package is to *build* and *manipulate* DAGs within a Django project. If you are looking for graph *analysis* or *visualization*, this may not be the right package.\n\nCurrently, django-postgresql-dag provides numerous methods for retrieving nodes, and a few for retrieving edges within the graph. In-progress are filters within the CTEs in order to limit the area of the graph to be searched, ability to easily export to NetworkX, and other improvements and utilities.\n\n## Demo\n\n[Quickstart example](https://django-postgresql-dag.readthedocs.io/en/latest/quickstart.html)\n\n## Install\n\n    pip install django-postgresql-dag\n\nWith optional dependencies for using transformations:\n\n    pip install django-postgresql-dag[transforms]\n\n\n## ToDo\n\nSee the checklists in [issues](https://github.com/OmenApps/django-postgresql-dag/issues) to understand the future goals of this project.\n\n\n## Credits:\n\n1. [This excellent blog post](https://www.fusionbox.com/blog/detail/graph-algorithms-in-a-database-recursive-ctes-and-topological-sort-with-postgres/620/)\n2. [django-dag](https://pypi.org/project/django-dag/)\n3. [django-dag-postgresql](https://github.com/worsht/django-dag-postgresql)\n4. [django-treebeard-dag](https://pypi.org/project/django-treebeard-dag/)\n",
    'author': 'Jack Linke',
    'author_email': 'jack@watervize.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/OmenApps/django-postgresql-dag',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
