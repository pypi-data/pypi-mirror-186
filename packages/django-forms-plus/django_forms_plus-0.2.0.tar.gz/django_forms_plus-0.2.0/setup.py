# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['django_forms_plus']

package_data = \
{'': ['*'], 'django_forms_plus': ['static/django_forms_plus/*']}

install_requires = \
['pydantic>=1.10.2,<2.0.0']

setup_kwargs = {
    'name': 'django-forms-plus',
    'version': '0.2.0',
    'description': 'React-powered forms for Django',
    'long_description': "# django_forms_plus (DPF)\n\nThe extendable ReactJS-powered rendering layer for Django Forms.\n\n## The state of the project\n**This package in in ALPHA state. DON'T USE ON PRODUCTION (or do it on your own risk).\nThe architecture and approaches can get changed significantly in next versions.**  \nAlso, there aren't so many supported fields and widgets for now\nsince it's just a proof of concept mostly.\n\n## Docs\nWill be available in next versions.\n\n## Dependencies\n\n### Javascript\n- react, react-dom\n- react-hook-form - [site](https://react-hook-form.com/)\n- yup - [npm](https://www.npmjs.com/package/yup)\n- classnames\n\n### Python\n- pydantic\n\n## License\nMIT\n",
    'author': 'Vladimir Sklyar',
    'author_email': 'versus.post@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/versusbassz/django_forms_plus',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
