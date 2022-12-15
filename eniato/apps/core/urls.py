from django.urls import path
from apps.core.views import (
    NotAuthorizedView,
    IndexView
)


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('nao-autorizado/', NotAuthorizedView.as_view(), name='not_authorized')
]
