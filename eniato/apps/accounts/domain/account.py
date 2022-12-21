from typing import Optional

from lib.users.domain import User
from lib.helpers import local_currency
from .financial_institution import FinancialInstitution

from apps.accounts.constants import ACCOUNT_TYPE_DISPLAY_NAME


class Account:
    """"
    Account for a specific user

    Attrs:
        - 
    """

    def __init__(self, attributes={}):
        self.id: Optional[int] = attributes.get('id')
        self.user: User = attributes['user']
        self.financial_institution: FinancialInstitution = attributes['financial_institution']
        self.opening_balance: float = attributes['opening_balance']
        self.current_balance: float = attributes.get('current_balance')
        self.description: str = attributes['description']
        self.account_type: str = attributes['account_type']
        self.color: str = attributes['color']
        self.default: bool = attributes['default']
        self.active: bool = attributes['active']

    def set_id(self, id):
        self.id = id

    def set_default(self, default):
        self.default = default

    @property
    def display_account_type(self):
        return dict(ACCOUNT_TYPE_DISPLAY_NAME)[self.account_type]

    @property
    def display_opening_balance(self):
        return local_currency(self.opening_balance)

    @property
    def display_current_balance(self):
        return local_currency(self.current_balance)
