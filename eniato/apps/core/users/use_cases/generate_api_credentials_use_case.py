from apps.core.users.domain.user import User
from apps.core.users.repositories.user_repository import UserRepository


class GenerateApiCredentialsUseCase:

    def __init__(self, user_repository=None):
        self.user_repository = user_repository or UserRepository()

    def execute(self, brnet_group_id, username):
        api_user = self.user_repository.get_by_brnet_group_id_and_user_name(
            brnet_group_id,
            username
        )

        if api_user:
            api_user.set_new_password()
        else:
            api_user = User.build_new(brnet_group_id, username)

        self.user_repository.save(api_user)

        return {
            'username': api_user.username,
            'password': api_user.password,
            'client_id': api_user.application.client_id,
            'client_secret': api_user.application.client_secret
        }
