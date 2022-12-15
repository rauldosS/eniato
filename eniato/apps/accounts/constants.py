from enum import Enum


class AccountType(Enum):
    CHECKING_ACCOUNT = 'checking_account'
    MONEY = 'money'
    SAVINGS = 'savings'
    INVESTMENTS = 'investments'
    OTHERS = 'others'

ACCOUNT_TYPE_CHECKING_ACCOUNT = 'checking_account'
ACCOUNT_TYPE_MONEY = 'money'
ACCOUNT_TYPE_SAVINGS = 'savings'
ACCOUNT_TYPE_INVESTMENTS = 'investments'
ACCOUNT_TYPE_OTHERS = 'others'

CHECKING_ACCOUNT_DISPLAY_NAME = 'Conta corrente'
MONEY_DISPLAY_NAME = 'Dinheiro'
SAVINGS_DISPLAY_NAME = 'Poupança'
INVESTMENTS_DISPLAY_NAME = 'Investimentos'
OTHERS_DISPLAY_NAME = 'Outros'

ACCOUNT_TYPES = {
    ACCOUNT_TYPE_CHECKING_ACCOUNT: CHECKING_ACCOUNT_DISPLAY_NAME,
    ACCOUNT_TYPE_MONEY: MONEY_DISPLAY_NAME,
    ACCOUNT_TYPE_SAVINGS: SAVINGS_DISPLAY_NAME,
    ACCOUNT_TYPE_INVESTMENTS: INVESTMENTS_DISPLAY_NAME,
    ACCOUNT_TYPE_OTHERS: OTHERS_DISPLAY_NAME,
}

ACCOUNT_TYPE_DISPLAY_NAME = (
    (AccountType.CHECKING_ACCOUNT.value, 'Conta corrente'),
    (AccountType.MONEY.value, 'Dinheiro'),
    (AccountType.SAVINGS.value, 'Poupança'),
    (AccountType.INVESTMENTS.value, 'Investimentos'),
    (AccountType.OTHERS.value, 'Outros'),
)
