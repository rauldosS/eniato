from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.accounts.repositories import AccountRepository


class AccountListView(LoginRequiredMixin, ListView):

    template_name = 'accounts/account-list.html'
    context_object_name = 'accounts'
    paginate_by = 3
    repository = AccountRepository()

    def get_queryset(self):
        return self.repository.get_by_user(self.request.user)
