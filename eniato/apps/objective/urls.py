from django.urls import path, include
from apps.objective.views import ObjectiveView
from apps.objective.views.rest import urls as rest_urls


urlpatterns = [
    path('', ObjectiveView.as_view(), name='home'),
    path('rest/', include((rest_urls, 'rest'), namespace='rest')),
]
