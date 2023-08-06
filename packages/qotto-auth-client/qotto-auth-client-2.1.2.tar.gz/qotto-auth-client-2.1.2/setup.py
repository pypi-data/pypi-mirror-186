# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['qottoauth', 'qottoauth.api']

package_data = \
{'': ['*']}

install_requires = \
['PyJWT>=2.0.0',
 'cryptography>=37.0.0',
 'eventy>=3.3.0',
 'gql[requests]>=2.0.0',
 'requests>=2.0.0']

setup_kwargs = {
    'name': 'qotto-auth-client',
    'version': '2.1.2',
    'description': 'Qotto/QottoAuthClient',
    'long_description': '# Qotto Auth Client\n\nThe python package `qotto-auth-client` is a client for the API `qotto-auth` which will soon be open sourced.\n\nIt allows to manage a scoped permission and authentication system.\n\nMore information coming soon...\n\n## Quickstart\n\nThe `QottoAuthService` class allows to interact with a `qotto-auth` GraphQL server.\n\n```python\nfrom qottoauth import *\n\n# Initialize the service\nqotto_auth_service = QottoAuthService(QottoAuthGqlApi(QOTTO_AUTH_URL)) \n\n# Register this application\napplication = qotto_auth_service.register_application(\n    name=APPLICATION_NAME,\n    description=APPLICATION_DESCRIPTION,\n)\n\n# Register permission\npermission_1 = qotto_auth_service.register_permission(\n    name=PERMISSION_1_NAME,\n    description=PERMISSION_1_DESCRIPTION,\n    application=application,\n)\n\n# Fetch current user or member\ndef handle(request)\n    actor = qotto_auth_service.actor(\n        token=request.COOKIES.get(TOKEN_COOKIE_NAME),\n        secret=request.COOKIES.get(SECRET_COOKIE_NAME),\n    )\n    if qotto_auth_service.is_authorized(\n        actor=actor,\n        permission=permission_1,\n    ):\n        # Do something\n    else:\n        # Do something else\n```\n\nYou can instantiate a `QottoAuthService` with a `QottoAuthTestApi` for testing purposes. In that case you might want to\nextend the test api class if you extended service using direct api calls.',
    'author': 'Qotto Dev Team',
    'author_email': 'dev@qotto.net',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
