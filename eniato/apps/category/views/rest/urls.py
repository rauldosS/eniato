from django.urls import path

from .get_all_categories_view import GetAllCategoriesView
from .get_categories_for_income_view import GetCatoriesForIncomeView
from .get_categories_for_expense_view import GetCatoriesForExpenseView

urlpatterns = [
    path(
        'categorias/todas',
        GetAllCategoriesView.as_view(),
        name='get_all_categories'
    ),
    path(
        'categorias/receita',
        GetCatoriesForIncomeView.as_view(),
        name='get_income_categories'
    ),
    path(
        'categorias/despesa',
        GetCatoriesForExpenseView.as_view(),
        name='get_expense_categories'
    )
]
