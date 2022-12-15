from lib.framework.users.mappers.user_mapper import UserMapper
import lib.framework.users.constants as C
from django.contrib.auth import get_user_model


class UserRepository:
    model = get_user_model()

    def __init__(self, user_mapper=None):
        self.user_mapper = user_mapper or UserMapper()

    def get_default_user(self):
        try:
            return self.user_mapper.map(
                self.model.objects.get(username=C.DEFAULT_USERNAME)
            )
        except Exception:
            return None
