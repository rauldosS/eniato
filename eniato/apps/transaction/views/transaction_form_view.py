from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages

from apps.transaction.models.transaction import Transaction
from apps.transaction.forms import TransactionForm

from apps.transaction.use_cases import CreateTransactionUseCase

from apps.transaction.constants import TRANSACTION_TYPE_BY_DISPLAY_NAME


class TransactionCreateView(LoginRequiredMixin, FormView):

    use_case = CreateTransactionUseCase()
    template_name = 'transaction/transaction-form.html'
    form_class = TransactionForm
    success_url = reverse_lazy('transaction:home')

    # def post(self, request, *args, **kwargs):
    #     print('kwargs', self.get_form_kwargs())
    #     form = TransactionForm(request.POST, *args, self.get_form_kwargs())
    #     print('post')
    #     print('valid', form.is_valid())
    #     print('data', form.data)
    #     print('cleaned_data', form.cleaned_data)
    #     print('form', form.errors)
    #     return super(TransactionCreateView, self).post(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(TransactionCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        kwargs['kwargs'] = self.kwargs
        return kwargs

    def form_valid(self, form):
        print('form', form.cleaned_data)
        self.use_case.execute(form.cleaned_data)
        return super().form_valid(form)
