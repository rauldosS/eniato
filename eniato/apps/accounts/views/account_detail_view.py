from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse

from apps.accounts.repositories import AccountRepository
from apps.core.services.user_access_service import UserVerifyAccess

from apps.accounts.models import Account


class AccountDetailView(LoginRequiredMixin, DetailView):
    model = Account
    template_name = 'accounts/account-detail.html'
    context_object_name = 'account'
    account_repository = AccountRepository()
    verify_user_access_service = UserVerifyAccess()

    def get(self, request, *args, **kwargs):
        if not self.verify_user_access_service.account_access(request.user, self.kwargs['pk']):
            return HttpResponseRedirect(reverse('accounts:home'))
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['account'] = self.account_repository.get_by_id(self.kwargs.get('pk'))

        return context
