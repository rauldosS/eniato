from enum import Enum


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
    INCOMING_TRANSFER = 'incoming_transfer'
    OUTGOING_TRANSFER = 'outgoing_transfer'

TRANSACTION_TYPE_DISPLAY_NAME = (
    (TransactionType.INCOME.value, 'Receita'),
    (TransactionType.EXPENSE.value, 'Despesa'),
    (TransactionType.CREDIT.value, 'Crédito'),
    (TransactionType.INCOMING_TRANSFER.value, 'Transferência entrada'),
    (TransactionType.OUTGOING_TRANSFER.value, 'Transferência saída'),
)

TRANSACTION_TYPE_BY_DISPLAY_NAME = (
    ('receita', TransactionType.INCOME.value),
    ('despesa', TransactionType.EXPENSE.value), 
    ('credito', TransactionType.CREDIT.value), 
    ('transferencia', TransactionType.INCOMING_TRANSFER.value), 
)

CATEGORY_TYPE_FOR_TRANSACTION_TYPE = (
    ('income', TransactionType.INCOME.value),
    ('expense', TransactionType.EXPENSE.value), 
    ('credit', TransactionType.EXPENSE.value), 
    ('transfer', TransactionType.INCOMING_TRANSFER.value), 
)

class RepeatPeriod(Enum):
    EVERY_DAY = 'everyday'
    WEEKLY = 'weekly'
    MONTHLY = 'monthly'
    ANNUALLY = 'annually'
    EVERY_DAY_WEEK = 'every_day_week'

REPEAT_EVERY_DISPLAY_NAME = (
    (RepeatPeriod.EVERY_DAY.value, 'Todos os dias'),
    (RepeatPeriod.WEEKLY.value, 'Semanalmente'),
    (RepeatPeriod.MONTHLY.value, 'Mensalmente'),
    (RepeatPeriod.ANNUALLY.value, 'Anualmente'),
    (RepeatPeriod.EVERY_DAY_WEEK.value, 'Todos os dias da semana'),
)
