from lib.users.factories import UserFactory

from apps.accounts.domain import Account
from .financial_institution_factory import FinancialInstitutionFactory


class AccountFactory:

    def __init__(self, user_factory=None, financial_institution_factory=None):
        self.user_factory = user_factory or UserFactory()
        self.financial_institution_factory = financial_institution_factory or FinancialInstitutionFactory()

    def create_from_data(self, data):
        attributes = {}

        attributes['id'] = data.get('id')
        attributes['user'] = data['user']
        attributes['financial_institution'] = data['financial_institution']
        attributes['opening_balance'] = data['opening_balance']
        attributes['current_balance'] = data['current_balance']
        attributes['description'] = data['description']
        attributes['account_type'] = data['account_type']
        attributes['color'] = data['color']
        attributes['default'] = data['default']

        return Account(attributes)

    def create_from_model(self, model):
        return Account({
            'id': model.id,
            'user': self.user_factory.create_from_user_model(model.user),
            'financial_institution': self.financial_institution_factory.create_from_model(model.financial_institution),
            'opening_balance': model.opening_balance,
            'current_balance': model.current_balance,
            'description': model.description,
            'account_type': model.account_type,
            'color': model.color,
            'default': model.default
        })
