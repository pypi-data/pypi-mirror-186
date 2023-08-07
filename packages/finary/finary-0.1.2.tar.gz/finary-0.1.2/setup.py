# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['finary']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.24.1,<2.0.0', 'openpyxl>=3.0.10,<4.0.0', 'pandas>=1.5.3,<2.0.0']

setup_kwargs = {
    'name': 'finary',
    'version': '0.1.2',
    'description': "Finary se compose de différents sous-modules ayant tous pour objectif d'augmenter la productivité d'un actuaire dans ses tâches du quotidien.",
    'long_description': "# Finary\n\n## À propos\n\n`Finary` se compose de différents sous-modules ayant tous pour objectif d'augmenter la productivité d'un actuaire dans ses tâches du quotidien.\n\n\n\n## Les projets\n\nVoici une liste non-exhaustive des idées à dates :\n\n* `matha` : calculs basiques d'actuariat (tx équivalent, valeur actuelle...)\n* `excel` : intéractions avec un fichier Excel améliorés (à partir des noms)\n* `model` : modèles financiers (black & Scholes, pricer option...)\n* `alm` : modèle ALM (gros projet)\n* `provisions` : méthodes basiques de provisionnement (chain ladder...)\n\n",
    'author': 'Mathieu Clavier',
    'author_email': 'mathieu.clavier@outlook.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
