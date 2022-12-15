from django.urls import path

from .get_categories_for_income import GetCatoriesForIncome
from .get_categories_for_expense import GetCatoriesForExpense

urlpatterns = [
    path(
        'categorias/receita',
        GetCatoriesForIncome.as_view(),
        name='get_income_categories'
    ),
    path(
        'categorias/despesa',
        GetCatoriesForExpense.as_view(),
        name='get_expense_categories'
    )
]
