from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.transaction.repositories.transaction_repository import TransactionRepository


class TransactionListView(LoginRequiredMixin, ListView):

    template_name = 'transaction/transaction-list.html'
    context_object_name = 'transactions'
    repository = TransactionRepository()

    def get_queryset(self):
        return self.repository.get_by_user(self.request.user, self.request.GET['month'], self.request.GET['year'])
