from typing import Optional

from lib.helpers import local_currency

from apps.category.domain import Category
from apps.accounts.domain import Account
from apps.transaction.domain.daily_balance import DailyBalance

from apps.transaction.constants import TransactionType


class Transaction:
    """
    """

    def __init__(self, attributes={}):
        self.id: Optional[int] = attributes.get('id')
  
        self.daily_balance: Optional[DailyBalance] = attributes.get('daily_balance')
        self.category: Category = attributes['category']
        self.account: Account = attributes['account']
        # self.credit_card: CreditCard = attributes['credit_card']
        # store
        # tag
        # recurrence: float = attributes['recurrence']

        self.installment: int = attributes.get('installment')
        self.value: float = attributes['value']
        self.description: str = attributes['description']
        self.transaction_date = attributes['transaction_date']
        self.transaction_type: str = attributes['transaction_type']

        self.status: bool = attributes.get('status', False)
        self.ignore: bool = attributes.get('ignore', False)

        # file
        self.observation: str = attributes['observation']

    def set_id(self, id):
        self.id = id

    @property
    def display_status(self):
        return 'Efetuada' if self.status else 'Pendente'

    @property
    def display_value(self):
        return local_currency(self.value)

    @property
    def display_account_logo(self):
        account = self.account
        return account.financial_institution.logo

    @property
    def display_account(self):
        account = self.account
        return f'{ account.description }'

    @property
    def value_for_transaction_type(self):
        if (self.transaction_type == TransactionType.INCOME.value) or (self.transaction_type == TransactionType.INCOMING_TRANSFER.value):
            return self.value
        return self.value * -1
