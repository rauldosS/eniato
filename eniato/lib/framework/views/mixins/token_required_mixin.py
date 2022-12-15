from django.conf import settings
from rest_framework.permissions import IsAuthenticated


class TokenRequiredMixin(object):

    permission_classes = (IsAuthenticated,)

    def __new__(cls, *args, **kwargs):
        cls = super(TokenRequiredMixin, cls).__new__(cls, *args, **kwargs)

        if not settings.DEV_ENVIRONMENT:
            return cls

        if hasattr(cls, "authentication_classes"):
            cls.authentication_classes += settings.DEV_ENVIRONMENT_SESSION_CLASSES

        else:
            cls.authentication_classes = settings.DEV_ENVIRONMENT_SESSION_CLASSES
        return cls
