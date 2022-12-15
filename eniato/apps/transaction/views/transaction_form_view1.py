from django.urls import reverse_lazy
from django.views.generic import FormView

from apps.transaction.forms import TransactionForm

from django.contrib.auth.mixins import LoginRequiredMixin


class TransactionFormView(LoginRequiredMixin, FormView):
    template_name = 'transaction/transaction-form.html'
    form_class = TransactionForm
    success_url = reverse_lazy('transaction:home')

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        ctx['username'] = self.username
        return ctx

    def form_valid(self, form):
        pass
