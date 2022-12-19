from django.urls import path, include
from apps.transaction.views import TransactionSummaryView
from apps.transaction.views.rest import urls as rest_urls

urlpatterns = [
    path('', TransactionSummaryView.as_view(), name='home'),
    path('rest/', include((rest_urls, 'rest'), namespace='rest')),
]
