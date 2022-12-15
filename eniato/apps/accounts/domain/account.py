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
        self.active: bool = attributes.get('active', True)
        self.include_on_dashboard: bool = attributes['include_on_dashboard']

    def set_id(self, id):
        self.id = id

    @property
    def display_account_type(self):
        return dict(ACCOUNT_TYPE_DISPLAY_NAME)[self.account_type]

    @property
    def display_opening_balance(self):
        return local_currency(self.opening_balance)

    @property
    def display_current_balance(self):
        return local_currency(self.current_balance)

    @property
    def display_default(self):
        return 'Sim' if self.default else 'Não'

    @property
    def display_active(self):
        return 'Sim' if self.active else 'Não'

    @property
    def display_include_on_dashboard(self):
        return 'Sim' if self.include_on_dashboard else 'Não'
