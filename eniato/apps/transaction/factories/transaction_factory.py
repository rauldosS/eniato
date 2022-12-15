from apps.transaction.domain.transaction import Transaction

from apps.category.factories import CategoryFactory
from apps.accounts.factories import AccountFactory


class TransactionFactory:

    def __init__(self, category_factory=None, account_factory=None):
        self.category_factory = category_factory or CategoryFactory()
        self.account_factory = account_factory or AccountFactory()

    def create_from_data(self, data):
        attributes = {}

        attributes['id'] = data.get('id')

        attributes['daily_balance'] = data.get('daily_balance')
        attributes['category'] = data['category']
        attributes['account'] = data['account']

        attributes['installment'] = data.get('installment')
        attributes['value'] = data['value']
        attributes['description'] = data['description']
        attributes['transaction_date'] = data['transaction_date']
        attributes['transaction_type'] = data['transaction_type']

        attributes['status'] = data['status']
        attributes['ignore'] = data['ignore']

        attributes['observation'] = data['observation']

        return Transaction(attributes)

    def create_from_model(self, model):
        return Transaction({
            'id': model.id,
            'category': self.category_factory.create_from_model(model.category),
            'account': self.account_factory.create_from_model(model.account),
            'installment': model.installment,
            'value': model.value,
            'description': model.description,
            'transaction_date': model.transaction_date,
            'transaction_type': model.transaction_type,
            'status': model.status,
            'ignore': model.ignore,
            'observation': model.observation,
        })
