from django.urls import path

from .get_transaction_list_view import GetTransactionListView
from .save_transaction_view import SaveTransactionView
from .delete_transaction_view import DeleteTransactionView


urlpatterns = [
    path(
        'transacoes',
        GetTransactionListView.as_view(),
        name='get_transaction_list_by_month'
    ),
    path(
        'salvar',
        SaveTransactionView.as_view(),
        name='create_transaction'
    ),
    path(
        'apagar/<transaction_id>',
        DeleteTransactionView.as_view(),
        name='delete_transaction'
    )
]
