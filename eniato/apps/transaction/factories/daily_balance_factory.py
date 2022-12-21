from apps.transaction.domain import DailyBalance

import decimal


class DailyBalanceFactory:

    def create_from_data(self, data):
        attributes = {}

        attributes['reference_date'] = data['reference_date']

        attributes['balance'] = data.get('balance', decimal.Decimal(0))
        attributes['income'] = data.get('income', decimal.Decimal(0))
        attributes['expense'] = data.get('expense', decimal.Decimal(0))
        attributes['credit'] = data.get('credit', decimal.Decimal(0))

        attributes['expected_balance'] = data.get('expected_balance', decimal.Decimal(0))
        attributes['expected_income'] = data.get('expected_income', decimal.Decimal(0))
        attributes['expected_expense'] = data.get('expected_expense', decimal.Decimal(0))
        attributes['expected_credit'] = data.get('expected_credit', decimal.Decimal(0))
        attributes['transactions'] = data.get('transactions', [])

        return DailyBalance(attributes)
