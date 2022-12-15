from lib.users.mappers.user_mapper import UserMapper
from lib.users import constants as C
from django.contrib.auth import get_user_model


class UserRepository:
    model = get_user_model()

    def __init__(self, user_mapper=None):
        self.user_mapper = user_mapper or UserMapper()

    def get_by_id(self, user_id):
        user_model = self.model.objects.get(id=user_id)
        return self.user_mapper.map(user_model)

    def get_by_username(self, username):
        user_model = self.model.objects.get(username=username)
        return self.user_mapper.map(user_model)

    def get_default_user(self):
        try:
            return self.user_mapper.map(
                self.model.objects.get(username=C.DEFAULT_USERNAME)
            )
        except Exception:
            return None

    def save(self, user_domain):
        user_model, created = self.model.objects.update_or_create(
            username=user_domain.username,
            defaults=dict(
                email=user_domain.email,
                first_name=user_domain.first_name,
                last_name=user_domain.last_name
            )
        )

        user_domain.set_id(user_model.id)

        return user_domain, created
