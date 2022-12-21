"""eniato URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

from apps.core import urls as core_urls
from apps.accounts import urls as accounts_urls
from apps.category import urls as category_urls
from apps.transaction import urls as transaction_urls
from apps.objective import urls as objective_urls

from apps.core.views import Http404View
from apps.core import views as myapp_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('contas/', include((accounts_urls, 'accounts'), namespace='accounts')),
    path('categorias/', include((category_urls, 'category'), namespace='category')),
    path('transacoes/', include((transaction_urls, 'transaction'), namespace='transaction')),
    path('objetivos/', include((objective_urls, 'objective'), namespace='objective')),
    path('accounts/', include('allauth.urls')),
    path('', include((core_urls, 'core'), namespace='core')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = Http404View.as_view()
handler500 = myapp_views.error_500
