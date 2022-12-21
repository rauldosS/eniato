from django.urls import path, include
from apps.accounts.views import AccountView
from apps.accounts.views.rest import urls as rest_urls


urlpatterns = [
    path('', AccountView.as_view(), name='home'),
    path('rest/', include((rest_urls, 'rest'), namespace='rest')),
]
