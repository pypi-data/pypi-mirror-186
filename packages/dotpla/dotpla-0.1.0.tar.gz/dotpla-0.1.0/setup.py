# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dotpla', 'dotpla.migrations']

package_data = \
{'': ['*']}

install_requires = \
['django>=3.2']

setup_kwargs = {
    'name': 'dotpla',
    'version': '0.1.0',
    'description': 'Django One Time Password Link Authentication',
    'long_description': "# dotpla: Django One Time Password Link Authentication\n\nThis app adds a new Authentication method to Django, which allows you to generate links with a one-time password so you can allow users to log in directly, without having to define a password. It is **not** an implementation of two-factor authentication (2FA).\n\n## Status\n\n**Warning:** this project is currently in development, and only supports Wagtail, for now. It is likely to change as/if I have time, but I am developing it primarily for my own uses, so it may not always be the highest priority.\n\n## Rationale and Use Cases\n\nThis app can be used to share data with selected users from the deep web, without requiring them to register or login. You can create the user account for them, generate a one-time password, and send them a link that will log them in automatically. This allows you to protect data from unauthorized access, but also makes it easy for end-users to access it.\n\nSome potential use cases:\n\n- Share a tailored version of your CV or cover letter with potential employers.\n- Write a tailored sales pitch for potential customers.\n- Share files with select users.\n\n## Installation\n\n### Pre-requirements\n\n- Django 3.2 or greater.\n- Python 3.8 or greater.\n- The [Django Messages Framework](https://docs.djangoproject.com/en/dev/ref/contrib/messages/) must be enabled for your project if you want passwords to be displayed in the admin interface.\n- *Optional:* [Wagtail CMS](https://wagtail.org/). Tested with Wagtail 4.0.\n\n## Usage\n\nTODO.\n\n## Caveats\n\n- The `authenticate_with_otp` method has potential race conditions allowing users to log in more times than they should. As I only use this with trusted users, it's insignificant enough for me to ignore.\n",
    'author': 'The Epic',
    'author_email': 'theepic.dev.83@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
