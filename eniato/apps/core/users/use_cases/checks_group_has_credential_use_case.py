from datetime import timezone

from apps.core.users.repositories.user_repository import UserRepository


class ChecksGroupHasCredentialUseCase:
    def __init__(self, user_repository=None):
        self.user_repository = user_repository or UserRepository()

    def execute(self, brnet_group_id, username):
        api_user = self.user_repository.get_by_company_group(brnet_group_id, username)
        if api_user:
            date_utc = api_user.modified_at.replace(tzinfo=timezone.utc).astimezone(tz=None)
            return {"date_last_credential": date_utc.strftime("%d/%m/%Y às %H:%M:%S")}
        else:
            return {
                "date_last_credential": None,
            }
