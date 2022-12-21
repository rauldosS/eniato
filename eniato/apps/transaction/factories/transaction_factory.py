from lib.users.factories import UserFactory

from apps.transaction.domain.transaction import Transaction

from apps.category.factories import CategoryFactory
from apps.accounts.factories import AccountFactory


class TransactionFactory:

    def __init__(self, category_factory=None, account_factory=None, user_factory=None):
        self.category_factory = category_factory or CategoryFactory()
        self.account_factory = account_factory or AccountFactory()
        self.user_factory = user_factory or UserFactory()

    def create_from_data(self, data):
        attributes = {}

        attributes['id'] = data.get('id')

        attributes['user'] = data['user']
        attributes['category'] = data['category']
        attributes['account'] = data['account']

        attributes['value'] = data['value']
        attributes['description'] = data['description']
        attributes['transaction_date'] = data['transaction_date']
        attributes['transaction_type'] = data['transaction_type']

        attributes['installment'] = data['installment']
        attributes['status'] = data['status']
        attributes['observation'] = data['observation']

        return Transaction(attributes)

    def create_from_model(self, model):
        return Transaction({
            'id': model.id,
            'user': self.user_factory.create_from_user_model(model.user),
            'category': self.category_factory.create_from_model(model.category),
            'account': self.account_factory.create_from_model(model.account),
            'value': model.value,
            'description': model.description,
            'transaction_date': model.transaction_date,
            'transaction_type': model.transaction_type,
            'installment': model.installment,
            'status': model.status,
            'observation': model.observation
        })
