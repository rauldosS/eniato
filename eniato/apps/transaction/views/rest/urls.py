from django.urls import path

from .get_transaction_list_view import GetTransactionListView
from .create_transaction_view import CreateTransactionView


urlpatterns = [
    path(
        'transacoes',
        GetTransactionListView.as_view(),
        name='get_transaction_list_by_month'
    ),
    path(
        'criar',
        CreateTransactionView.as_view(),
        name='create_transaction'
    )
]
