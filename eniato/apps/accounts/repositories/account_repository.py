from lib.framework.models.base_repository import BaseRepository

from apps.accounts.factories import AccountFactory
from apps.accounts.models.account import Account
from apps.accounts.domain import Account as AccountDomain


class AccountRepository(BaseRepository):

    def __init__(self, model=None, domain_object=None, factory=None):
        self.model = model or Account
        self.domain_object = domain_object or AccountDomain
        self.factory = factory or AccountFactory()

    def get_by_user(self, user):
        accounts = self.model.objects.filter(user=user).order_by('default', 'description')
        return [
            self.factory.create_from_model(account)
            for account in accounts
        ]

    def get_model_by_user(self, user):
        return self.model.objects.filter(user=user).order_by('default', 'description')

    def get_by_user_and_id(self, user, id):
        try:
            account = self.model.objects.get(id=id, user=user)
            return self.factory.create_from_model(account)
        except self.model.DoesNotExist:
            return None

    def update_current_balance(self, account, current_balance):
        self.model.stored.filter(id=account.id).update(
            current_balance=current_balance
        )

    def create(self, account_domain):
        account_model = self.model.stored.create(
            user_id=account_domain.user.id,
            financial_institution_id=account_domain.financial_institution.id,
            opening_balance=account_domain.opening_balance,
            current_balance=account_domain.current_balance,
            description=account_domain.description,
            account_type=account_domain.account_type,
            color=account_domain.color,
            default=account_domain.default,
            active=account_domain.active,
            include_on_dashboard=account_domain.include_on_dashboard,
        )

        account_domain.set_id(account_model.id)

        return account_domain

    """
    def save(self, account_domain):
        account_model, created = self.model.stored.update_or_create(
            id=account_domain.id,
            defaults=dict(
                user=account_domain.user,
                financial_institution=account_domain.financial_institution.id,
                opening_balance=account_domain.opening_balance,
                current_balance=account_domain.current_balance,
                description=account_domain.description,
                account_type=account_domain.account_type,
                color=account_domain.color,
                default=account_domain.default,
                active=account_domain.active,
                include_on_dashboard=account_domain.include_on_dashboard,
            )
        )

        if created:
            account_domain.set_id(account_model.id)

        return account_domain, created
    """