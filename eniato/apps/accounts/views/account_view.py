from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class AccountView(TemplateView, LoginRequiredMixin):
    template_name = 'accounts/account.html'
