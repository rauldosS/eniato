from rest_framework.authentication import (BasicAuthentication,
                                           SessionAuthentication,
                                           TokenAuthentication)

from .base import INSTALLED_APPS, config

DEV_ENVIRONMENT = config('DEV_ENVIRONMENT', default=False, cast=bool)

DEV_ENVIRONMENT_SESSION_CLASSES = (
    BasicAuthentication, SessionAuthentication, TokenAuthentication
)

DEV_APPS = [
]

if DEV_ENVIRONMENT:
    INSTALLED_APPS += DEV_APPS
