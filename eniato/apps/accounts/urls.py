from django.urls import path, include
from apps.accounts.views import (
    AccountListView,
    AccountDetailView,
    AccountCreateView,
    AccountUpdateView,
)
from apps.accounts.views.rest import urls as rest_urls


urlpatterns = [
    path('', AccountListView.as_view(), name='home'),
    path('cadastrar/', AccountCreateView.as_view(), name='create'),
    path('<pk>/', AccountDetailView.as_view(), name='detail'),
    path('<pk>/editar/', AccountUpdateView.as_view(), name='update'),
    path('rest/', include((rest_urls, 'rest'), namespace='rest')),
]
