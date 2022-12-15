from typing import Optional

from apps.transaction.constants import TransactionType


class DailyBalance:
    """
    """

    def __init__(self, attributes={}):
        self.id = attributes.get('id')
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

    def set_id(self, id):
        self.id = id

    def update_only_balance(self, transaction):
        if transaction.status:
            self.balance += transaction.value_for_transaction_type
        else:
            self.expected_balance += transaction.value_for_transaction_type

    def update_balance(self, transaction):
        if transaction.transaction_type == TransactionType.INCOME.value:
            self.set_income(transaction.value) if transaction.status else self.set_expected_income(transaction.value)

        if transaction.transaction_type == TransactionType.EXPENSE.value:
            self.set_expense(transaction.value) if transaction.status else self.set_expected_expense(transaction.value)

        if transaction.transaction_type == TransactionType.CREDIT.value:
            self.set_credit(transaction.value) if transaction.status else self.set_expected_credit(transaction.value)

        self.balance = self.income - (self.expense + self.credit)
        self.expected_balance = (self.expected_income + self.balance) - (self.expected_expense + self.expected_credit)

    def set_income(self, value):
        self.income += value

    def set_expected_income(self, value):
        self.expected_income += value

    def set_expense(self, value):
        self.expense += value

    def set_expected_expense(self, value):
        self.expected_expense += value

    def set_credit(self, value):
        self.credit += value

    def set_expected_credit(self, value):
        self.expected_credit += value
