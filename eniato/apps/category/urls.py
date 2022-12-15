from django.urls import path, include
from apps.category.views import (
    CategoryListView
)
from apps.category.views.rest import urls as rest_urls


urlpatterns = [
    path('', CategoryListView.as_view(), name='home'),
    path('rest/', include((rest_urls, 'rest'), namespace='rest')),
]
