# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['django_accounts_api', 'django_accounts_api.migrations']

package_data = \
{'': ['*'], 'django_accounts_api': ['templates/django_accounts_api/*']}

extras_require = \
{':python_version < "3.8"': ['django>=3.2'],
 ':python_version >= "3.8"': ['django>=3.2,<4.2']}

setup_kwargs = {
    'name': 'django-accounts-api',
    'version': '0.1.5',
    'description': '',
    'long_description': "# Django Accounts API\n\nScenario to support is a compiled javascript capable frontend needing to provide authentication features over api\n\nCaveat enptor, very early days, still being tested in it's first project\n\n# Requirements\n- Python 3.7 - 3.11\n- Django 3.2 - 4\n\n# Usage\n\n- `pip install ...` or equivalent\n- add `'django_accounts_api',` to INSTALLED_APPS\n- add `path('/accounts_api/', include('django_accounts_api.urls'))` to your urls\n- implement your frontend to use the urls\n\n## Features\n\nSee docs...\n\n\n## Development\n1. Install Poetry https://python-poetry.org/docs/#installation\n\n2. Use a virtual environment https://python-poetry.org/docs/basic-usage/#using-your-virtual-environment\n\n3. `poetry install --with dev --no-root` installs dependencies for development\n\n4. `poetry run pre-commit install` installs the pre-commit hooks\n\n5. `pytest` runs tests\n\n### Tox\n\nTo run tox you will need to make sure that the range of python versions required are available for tox to use.\n\nRecommendation: use pyenv\n- `pyenv install 3.7 3.8 3.9 3.10 3.11`\n- `pyenv local  3.7 3.8 3.9 3.10 3.11`\n- `tox`\n\n### Documentation\n\n- `cd docs`\n- `make html`\n\nTODO: add to tox\n\n### Linting & formatting\n\nTODO: add to tox\n",
    'author': 'PeteCoward',
    'author_email': 'peter@catalpa.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
