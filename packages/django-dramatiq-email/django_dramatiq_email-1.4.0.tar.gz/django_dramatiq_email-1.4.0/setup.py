# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['django_dramatiq_email']

package_data = \
{'': ['*']}

install_requires = \
['django<4.2', 'django_dramatiq>0.9,<1.0', 'dramatiq>=1.13.0,<2.0.0']

setup_kwargs = {
    'name': 'django-dramatiq-email',
    'version': '1.4.0',
    'description': 'A Django email backend using Dramatiq to send emails using background workers',
    'long_description': '# Django Dramatiq Email\n\nEmail backend for Django sending emails via Dramatiq.\n\nThis package is tested up to Django 4.1.\n\n[![Test Status](https://github.com/SendCloud/django-dramatiq-email/workflows/Test/badge.svg?branch=master)](https://github.com/SendCloud/django-dramatiq-email/actions?query=workflow%3ATest)\n[![Lint Status](https://github.com/SendCloud/django-dramatiq-email/workflows/Lint/badge.svg?branch=master)](https://github.com/SendCloud/django-dramatiq-email/actions?query=workflow%3ALint)\n[![Code coverage Status](https://codecov.io/gh/SendCloud/django-dramatiq-email/branch/master/graph/badge.svg)](https://codecov.io/gh/SendCloud/django-dramatiq-email)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n\n## Installation\n\nTo enable `django-dramatiq-email`, modify your project `settings.py`:\n\n- Add `"django_dramatiq_email"` to `INSTALLED_APPS` below `"django_dramatiq"`,\n- Set `EMAIL_BACKEND` to `"django_dramatiq_email.backends.DramatiqEmailBackend"`,\n- Set `DRAMATIQ_EMAIL_BACKEND` to the actual email backend you want to use (SMTP, Anymail, etc),\n- Optionally, add the `DRAMATIQ_EMAIL_TASK_CONFIG` dict as shown below.\n\n## Configuration\n\nThe `dramatiq.actor` args ([reference](https://dramatiq.io/reference.html#dramatiq.actor), [user guide](https://dramatiq.io/guide.html)) for `send_email` can be set via the `DRAMATIQ_EMAIL_TASK_CONFIG` dict in your `settings.py`.\n\nThe default args are [here](django_dramatiq_email/tasks.py) - most notably, the default `queue_name` is `django_email`.\n\nExample configuration (using the Retry middleware):\n\n```python\nDRAMATIQ_EMAIL_TASK_CONFIG = {\n    "max_retries": 20,\n    "min_backoff": 15000,\n    "max_backoff": 86400000,\n    "queue_name": "my_custom_queue"\n}\n```\n\n## Bulk emails\nBulk emails are send using individual Dramatiq tasks. Doing so these tasks can be restarted individually.\n\n## Maintainer\n[Tim Drijvers](http://github.com/timdrijvers)\n',
    'author': 'Tim Drijvers',
    'author_email': 'tim@sendcloud.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/sendcloud/django-dramatiq-email',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
