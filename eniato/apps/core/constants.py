from enum import Enum

class FinancialInstitutionType(Enum):
    CHECKING_ACCOUNT = 'checking_account'
    MONEY = 'money'
    SAVINGS = 'savings'
    INVESTMENTS = 'investments'
    OTHERS = 'others'

FINANCIAL_INSTITUTION_TYPE_DISPLAY_NAME = (
    (FinancialInstitutionType.CHECKING_ACCOUNT.value, 'Conta corrente'),
    (FinancialInstitutionType.MONEY.value, 'Dinheiro'),
    (FinancialInstitutionType.SAVINGS.value, 'Poupança'),
    (FinancialInstitutionType.INVESTMENTS.value, 'Investimentos'),
    (FinancialInstitutionType.OTHERS.value, 'Outros'),
)


class PaymentMethodType(Enum):
    CREDIT = 'credit'
    DEBIT = 'debit'
    BANK_SLIP = 'bank_slip'
    CASH = 'cash'
    PIX = 'pix'


CARD_TYPE_DISPLAY_NAME = (
    (PaymentMethodType.CREDIT.value, 'Crédito'),
    (PaymentMethodType.DEBIT.value, 'Débito'),
    (PaymentMethodType.BANK_SLIP.value, 'Boleto bancário'),
    (PaymentMethodType.CASH.value, 'Dinheiro'),
    (PaymentMethodType.PIX.value, 'Pix'),
)


class TransactionType(Enum):
    INCOME = 'income'
    EXPENSE = 'expense'
    CREDIT = 'credit'
    TRANSFER = 'transfer'

CATEGORY_TYPE_DISPLAY_NAME = (
    (TransactionType.INCOME.value, 'Receita'),
    (TransactionType.EXPENSE.value, 'Despesa'),
    (TransactionType.CREDIT.value, 'Crédito'),
    (TransactionType.TRANSFER.value, 'Transferência'),
)


class Color(Enum):
    """
        https://flatuicolors.com/palette/ca
    """
    JIGGLYPUFF = '#ff9ff3'
    LIAN_HONG_LOTUS_PINK = '#f368e0'
    CASANDORA_YELLOW = '#feca57'
    DOUBLE_DRAGON_SKIN = '#ff9f43'
    PASTEL_RED = '#ff6b6b'
    AMOUR = '#ee5253'
    MEGAMAN = '#48dbfb'
    CYANITE = '#0abde3'
    WILD_CARIBBEAN_GREEN = '#1dd1a1'
    DARK_MOUNTAIN_MEADOW = '#10ac84'
    JADE_DUST = '#00d2d3'
    AQUA_VELVET = '#01a3a4'
    JOUST_BLUE = '#54a0ff'
    BLEU_DE_FRANCE = '#2e86de'
    NASU_PURPLE = '#5f27cd'
    BLUEBELL = '#341f97'
    LIGHT_BLUE_BALLERINA = '#c8d6e5'
    STORM_PETREL = '#8395a7'
    FUEL_TOWN = '#576574'
    IMPERIAL_PRIMER = '#222f3e'

COLOR_DISPLAY_NAME = (
    (Color.JIGGLYPUFF.value, 'Jigglypuff'),
    (Color.CASANDORA_YELLOW.value, 'Casandora Yellow'),
    (Color.PASTEL_RED.value, 'Pastel Red'),
    (Color.MEGAMAN.value, 'Megaman'),
    (Color.WILD_CARIBBEAN_GREEN.value, 'Wil Caribbean Green'),
    (Color.LIAN_HONG_LOTUS_PINK.value, 'Lián Hón Lotus Pink'),
    (Color.DOUBLE_DRAGON_SKIN.value, 'Doubl Dragon Skin'),
    (Color.AMOUR.value, 'Amour'),
    (Color.CYANITE.value, 'Cyanite'),
    (Color.DARK_MOUNTAIN_MEADOW.value, 'Dar Mountain Meadow'),
    (Color.JADE_DUST.value, 'Jade Dust'),
    (Color.JOUST_BLUE.value, 'Joust Blue'),
    (Color.NASU_PURPLE.value, 'Nasu Purple'),
    (Color.LIGHT_BLUE_BALLERINA.value, 'Ligh Blue Ballerina'),
    (Color.FUEL_TOWN.value, 'Fuel Town'),
    (Color.AQUA_VELVET.value, 'Aqua Velvet'),
    (Color.BLEU_DE_FRANCE.value, 'Ble De France'),
    (Color.BLUEBELL,'Bluebell'),
    (Color.STORM_PETREL.value, 'Storm Petrel'),
)

class Icon(Enum):
    """
        https://icons.getbootstrap.com/
    """
    pass


class RecurrenceType(Enum):
    INCOME = 'income'
