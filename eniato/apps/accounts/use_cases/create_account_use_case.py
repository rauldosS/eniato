from apps.accounts.repositories import AccountRepository

from apps.accounts.factories import AccountFactory
from apps.accounts.repositories import FinancialInstitutionRepository
from lib.users.repositories.user_repository import UserRepository


class CreateAccountUseCase:

    def __init__(self, account_repository=None, account_factory=None, financial_institution_repository=None, user_repository=None):
        self.account_repository = account_repository or AccountRepository()
        self.account_factory = account_factory or AccountFactory()
        self.financial_institution_repository = financial_institution_repository or FinancialInstitutionRepository()
        self.user_repository = user_repository or UserRepository()

    def execute(self, user, form):
        print('form', form)
        # account_data = self._map_account(form)

        financial_institution_domain = self.financial_institution_repository.get_by_id(form['financial_institution'])
        user_domain = self.user_repository.get_by_username(user)

        opening_balance = float(form.get('opening_balance', 0.00).replace(".", "").replace(",", "."))

        account_domain = self.account_factory.create_from_data({
            'user': user_domain,
            'financial_institution': financial_institution_domain,
            'opening_balance': opening_balance,
            'current_balance': opening_balance,
            'description': form.get('description'),
            'account_type': form.get('account_type'),
            'color': form.getlist('color')[0],
            'active': True,
            'default': bool(form.get('default')),
            'include_on_dashboard': bool(form.get('include_on_dashboard')),
        })

        print('domain', account_domain.__dict__)
        # float(form['opening_balance'].replace(".", "").replace(",", ".")),

        return self.account_repository.create(account_domain)

