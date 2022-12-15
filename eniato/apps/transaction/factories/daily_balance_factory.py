from apps.transaction.domain import DailyBalance

from apps.transaction.factories.transaction_factory import TransactionFactory

import decimal


class DailyBalanceFactory:

    def __init__(self, transaction_factory=None):
        self.transaction_factory = transaction_factory or TransactionFactory()

    def create_from_data(self, data):
        attributes = {}

        attributes['id'] = data.get('id')
        attributes['reference_date'] = data['reference_date']

        attributes['balance'] = data.get('balance', decimal.Decimal(0))
        attributes['income'] = data.get('income', decimal.Decimal(0))
        attributes['expense'] = data.get('expense', decimal.Decimal(0))
        attributes['credit'] = data.get('credit', decimal.Decimal(0))

        attributes['expected_balance'] = data.get('expected_balance', decimal.Decimal(0))
        attributes['expected_income'] = data.get('expected_income', decimal.Decimal(0))
        attributes['expected_expense'] = data.get('expected_expense', decimal.Decimal(0))
        attributes['expected_credit'] = data.get('expected_credit', decimal.Decimal(0))

        return DailyBalance(attributes)

    def create_from_model(self, model, map_transactions=False):
        daily_balance = DailyBalance({
            'id': model.id,
            'reference_date': model.reference_date,
            'balance': model.balance,
            'income': model.income,
            'expense': model.expense,
            'credit': model.credit,
            'expected_balance': model.expected_balance,
            'expected_income': model.expected_income,
            'expected_expense': model.expected_expense,
            'expected_credit': model.expected_credit
        })

        if map_transactions:
            daily_balance.transactions = self._map_transactions(model.transaction_set.all())

        return daily_balance

    def create_from_previous_daily_balance(self, reference_date, model):
        return DailyBalance({
            'reference_date': reference_date,
            'balance': model.balance,
            'income': model.income,
            'expense': model.expense,
            'credit': model.credit,
            'expected_balance': model.expected_balance,
            'expected_income': model.expected_income,
            'expected_expense': model.expected_expense,
            'expected_credit': model.expected_credit
        })

    def _map_transactions(self, transactions):
        return [self.transaction_factory.create_from_model(transaction) for transaction in transactions]
