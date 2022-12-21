from django.urls import path

from .get_all_accounts_by_user_view import GetAllAccountsByUserView
from .get_all_financial_institutions_view import GetAllFinancialInstitutionsView
from .save_account_view import SaveAccountView
from .active_account_view import ActivateAccountView
from .deactivate_account_view import DeactivateAccountView
from .delete_account_view import DeleteAccountView

urlpatterns = [
    path(
        'contas/usuario',
        GetAllAccountsByUserView.as_view(),
        name='get_account_list_by_user'
    ),
    path(
        'salvar',
        SaveAccountView.as_view(),
        name='save_account'
    ),
    path(
        'instituicoes-financeiras',
        GetAllFinancialInstitutionsView.as_view(),
        name='get_all_financial_institutions'
    ),
    path(
        'ativar/<int:account_id>',
        ActivateAccountView.as_view(),
        name='activate_account_view'
    ),
    path(
        'desativar/<int:account_id>',
        DeactivateAccountView.as_view(),
        name='delete_account_view'
    ),
    path(
        'apagar/<int:account_id>',
        DeleteAccountView.as_view(),
        name='delete_account_view'
    )
]
