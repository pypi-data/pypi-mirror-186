# Qotto Auth Client

The python package `qotto-auth-client` is a client for the API `qotto-auth` which will soon be open sourced.

It allows to manage a scoped permission and authentication system.

More information coming soon...

## Quickstart

The `QottoAuthService` class allows to interact with a `qotto-auth` GraphQL server.

```python
from qottoauth import *

# Initialize the service
qotto_auth_service = QottoAuthService(QottoAuthGqlApi(QOTTO_AUTH_URL)) 

# Register this application
application = qotto_auth_service.register_application(
    name=APPLICATION_NAME,
    description=APPLICATION_DESCRIPTION,
)

# Register permission
permission_1 = qotto_auth_service.register_permission(
    name=PERMISSION_1_NAME,
    description=PERMISSION_1_DESCRIPTION,
    application=application,
)

# Fetch current user or member
def handle(request)
    actor = qotto_auth_service.actor(
        token=request.COOKIES.get(TOKEN_COOKIE_NAME),
        secret=request.COOKIES.get(SECRET_COOKIE_NAME),
    )
    if qotto_auth_service.is_authorized(
        actor=actor,
        permission=permission_1,
    ):
        # Do something
    else:
        # Do something else
```

You can instantiate a `QottoAuthService` with a `QottoAuthTestApi` for testing purposes. In that case you might want to
extend the test api class if you extended service using direct api calls.