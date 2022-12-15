from lib.users.domain import User


class UserFactory:

    def create_from_data(self, data):
        return User(
            id=data.get('id'),
            username=data.get('username'),
            email=data.get('email'),
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
        )

    def create_from_user_model(self, user_model):
        return User(
            id=user_model.id,
            username=user_model.username,
            email=user_model.email,
            first_name=user_model.first_name,
            last_name=user_model.last_name,
        )
