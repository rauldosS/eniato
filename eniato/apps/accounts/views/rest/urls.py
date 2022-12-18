from django.urls import path

# from .delete_account_view import ShelveAccountView
from .get_account_list_by_user_view import GetAccountListByUserView
from .get_all_financial_institutions_view import GetAllFinancialInstitutionsView
from .save_account_view import SaveAccountView
from .delete_account_view import DeleteAccountView

urlpatterns = [
    path(
        'contas/usuario',
        GetAccountListByUserView.as_view(),
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
        'apagar/<int:account_id>',
        DeleteAccountView.as_view(),
        name='delete_account_view'
    )
]
