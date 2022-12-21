from lib.framework.models.base_repository import BaseRepository

from apps.accounts.factories import AccountFactory
from apps.accounts.models.account import Account
from apps.accounts.domain import Account as AccountDomain


class AccountRepository(BaseRepository):

    def __init__(self, model=None, domain_object=None, factory=None):
        self.model = model or Account
        self.domain_object = domain_object or AccountDomain
        self.factory = factory or AccountFactory()

    def get_all_by_user(self, user):
        accounts = self.model.stored.filter(
            user=user
        ).order_by('-default', 'description')
        return [
            self.factory.create_from_model(account)
            for account in accounts
        ]

    def get_account_default(self, user):
        try:
            return self.factory.create_from_model(
                self.model.stored.get(user=user.id, default=True)
            )
        except self.model.DoesNotExist:
            return None

    def reset_default_account(self):
        self.model.stored.filter(default=True).update(default=False)

    def get_model_by_user(self, user):
        return self.model.stored.filter(user=user).order_by('default', 'description')

    def get_by_user_and_id(self, user, id):
        try:
            return self.factory.create_from_model(
                self.model.stored.get(id=id, user=user)
            )
        except self.model.DoesNotExist:
            return None

    def update_current_balance(self, account, balance):
        self.model.stored.filter(id=account.id).update(
            current_balance=balance
        )

    def user_have_default_account(self, user):
        return self.model.stored.filter(user=user.id, default=True).exists()

    def save(self, domain):
        account_model, created = self.model.stored.update_or_create(
            id=domain.id,
            defaults=dict(
                user_id=domain.user.id,
                financial_institution_id=domain.financial_institution.id,
                opening_balance=domain.opening_balance,
                current_balance=domain.current_balance,
                description=domain.description,
                account_type=domain.account_type,
                color=domain.color,
                default=domain.default
            )
        )

        if created:
            domain.set_id(account_model.id)

        return domain

    def update_account_activation(self, account_id, active):
        self.model.stored.filter(id=account_id).update(active=active)
