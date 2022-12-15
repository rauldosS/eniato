from enum import Enum


class CategoryType(Enum):
    INCOME = 'income'
    EXPENSE = 'expense'
   
CATEGORY_TYPE_DISPLAY_NAME = (
    (CategoryType.INCOME.value, 'Receita'),
    (CategoryType.EXPENSE.value, 'Despesa'),
)

CATEGORY_TYPE_EXPENSE = 'expense'
CATEGORY_TYPE_INCOME = 'income'

EXPENSE_DISPLAY_NAME = 'Despesa'
INCOME_DISPLAY_NAME = 'Receita'
