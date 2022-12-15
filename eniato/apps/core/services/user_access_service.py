
from apps.accounts.repositories import AccountRepository


class UserVerifyAccess:
    def __init__(self, account_repository=None):
        self.account_repository = account_repository or AccountRepository()

    def account_access(self, user, account_id):
        if user.is_superuser:
            return True

        if self.account_repository.get_by_user_and_id(user, account_id):
            return True
        return False
