# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['django_google_sso', 'django_google_sso.migrations', 'django_google_sso.tests']

package_data = \
{'': ['*'], 'django_google_sso': ['templates/admin_sso/*']}

install_requires = \
['django>=3.2',
 'google-auth',
 'google-auth-httplib2',
 'google-auth-oauthlib',
 'loguru']

setup_kwargs = {
    'name': 'django-google-sso',
    'version': '2.3.1',
    'description': 'Easily add Google SSO login to Django Admin',
    'long_description': '<p align="center">\n  <img src="docs/images/django-google-sso.png" alt="Django Google SSO"/>\n</p>\n\n[![PyPI](https://img.shields.io/pypi/v/django-google-sso)](https://pypi.org/project/django-google-sso/)\n[![Build](https://github.com/chrismaille/django-google-sso/workflows/tests/badge.svg)](https://github.com/chrismaille/django-google-sso/actions)\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/django-google-sso)](https://www.python.org)\n[![PyPI - Django Version](https://img.shields.io/pypi/djversions/django-google-sso)](https://www.djangoproject.com/)\n[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg)](https://conventionalcommits.org)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)\n\n## Welcome to Django Google SSO\n\nThis library aims to simplify the process of authenticating users with Google in Django Admin pages,\ninspired by libraries like [django_microsoft_auth](https://github.com/AngellusMortis/django_microsoft_auth)\nand [django-admin-sso](https://github.com/matthiask/django-admin-sso/)\n\n---\n\n### Documentation\n\n* Docs: https://chrismaille.github.io/django-google-sso/\n\n---\n\n### Install\n\n```shell\n$ pip install django-google-sso\n```\n\n### Configure\n\n1. Add the following to your `settings.py` `INSTALLED_APPS`:\n\n```python\n# settings.py\n\nINSTALLED_APPS = [\n    # other django apps\n    "django.contrib.messages",  # Need for Auth messages\n    "django_google_sso",  # Add django_google_sso\n]\n```\n\n2. In [Google Console](https://console.cloud.google.com/apis/credentials) at _Api -> Credentials_, retrieve your\n   Project Credentials and add them in your `settings.py`:\n\n```python\n# settings.py\n\nGOOGLE_SSO_CLIENT_ID = "your client id here"\nGOOGLE_SSO_PROJECT_ID = "your project id here"\nGOOGLE_SSO_CLIENT_SECRET = "your client secret here"\n```\n\n3. Add the callback uri `http://localhost:8000/google_sso/callback/` in your Google Console, on the "Authorized Redirect URL".\n\n4. Let Django Google SSO auto create users for allowable domains:\n\n```python\n# settings.py\n\nGOOGLE_SSO_ALLOWABLE_DOMAINS = ["example.com"]\n```\n\n5. In `urls.py` please add the **Django-Google-SSO** views:\n\n```python\n# urls.py\n\nfrom django.urls import include, path\n\nurlpatterns = [\n    # other urlpatterns...\n    path(\n        "google_sso/", include("django_google_sso.urls", namespace="django_google_sso")\n    ),\n]\n```\n6. And run migrations:\n\n```shell\n$ python manage.py migrate\n```\n\nThat\'s it. Start django on port 8000 and open your browser in `http://localhost:8000/admin/login` and you should see the Google SSO button.\n\n![](docs/images/django_login_with_google_white.png)\n\n---\n\n## License\n\nThis project is licensed under the terms of the MIT license.\n',
    'author': 'Chris Maillefaud',
    'author_email': 'chrismaillefaud@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/chrismaille/django-google-sso',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
