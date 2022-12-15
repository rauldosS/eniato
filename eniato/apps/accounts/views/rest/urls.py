from django.urls import path

from .shelve_account_view import ShelveAccountView
from .get_account_list_by_user_view import GetAccountListByUserView


urlpatterns = [
    path(
        'conta/<int:account_id>/arquivar',
        ShelveAccountView.as_view(),
        name='shelve_account'
    ),
    path(
        'contas/usuario',
        GetAccountListByUserView.as_view(),
        name='get_account_list_by_user'
    )
]
