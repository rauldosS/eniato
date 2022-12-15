from django.urls import path, include
from apps.transaction.views import (
    TransactionView,
    TransactionListView,
    TransactionCreateView
)
from apps.transaction.views.rest import urls as rest_urls

urlpatterns = [
    path('', TransactionView.as_view(), name='home'),
    path('cadastrar', TransactionCreateView.as_view(), name='cadastrar'),
    path('rest/', include((rest_urls, 'rest'), namespace='rest')),
]
