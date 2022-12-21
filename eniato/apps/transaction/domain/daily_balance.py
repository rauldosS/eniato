from typing import Optional

from apps.transaction.constants import TransactionType


class DailyBalance:
    """
    """

    def __init__(self, attributes={}):
        self.reference_date = attributes['reference_date']

        self.balance = attributes['balance']
        self.income = attributes['income']
        self.expense = attributes['expense']
        self.credit = attributes['credit']

        self.expected_balance = attributes['expected_balance']
        self.expected_income = attributes['expected_income']
        self.expected_expense = attributes['expected_expense']
        self.expected_credit = attributes['expected_credit']

        self.transactions = attributes.get('transactions')
