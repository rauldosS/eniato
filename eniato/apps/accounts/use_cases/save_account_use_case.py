from apps.accounts.domain import Account as AccountDomain

from apps.accounts.repositories import (
    AccountRepository,
    FinancialInstitutionRepository
)
from apps.accounts.factories import AccountFactory
from lib.users.repositories import UserRepository


class SaveAccountUseCase(object):

    def __init__(self, repository=None, factory=None, user_repository=None, financial_institution_repositovy=None):
        self.repository = repository or AccountRepository()
        self.factory = factory or AccountFactory()
        self.user_repository = user_repository or UserRepository()
        self.financial_institution_repositovy = financial_institution_repositovy or FinancialInstitutionRepository()

    def execute(self, user, form) -> AccountDomain:
        financial_institution_domain = self.financial_institution_repositovy.get_by_id(form['financial_institution_id'])
        user_domain = self.user_repository.get_by_id(user.id)

        account_domain = self.factory.create_from_data({
            'id': form['id'],
            'user': user_domain,
            'financial_institution': financial_institution_domain,
            'opening_balance': form['opening_balance'],
            'current_balance': form['opening_balance'],
            'description': form['description'],
            'account_type': form['account_type'],
            'color': form['color'],
            'default': form['default'],
            'active': form['active']
        })

        account_domain = self._set_default_account(account_domain, user_domain)
        self.repository.save(account_domain)

        return account_domain

    def _set_default_account(self, account_domain, user_domain):
        user_have_default_account = self.repository.user_have_default_account(user_domain)
        if not user_have_default_account:
            account_domain.set_default(True)
            return account_domain
        elif user_have_default_account and account_domain.default:
            self.repository.reset_default_account()
        return account_domain
