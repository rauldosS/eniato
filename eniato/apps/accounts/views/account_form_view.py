from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib import messages

from apps.accounts.models.account import Account
from apps.accounts.forms import AccountForm


class AccountCreateView(LoginRequiredMixin, CreateView):

    template_name = 'accounts/account-form.html'
    form_class = AccountForm
    success_url = reverse_lazy('accounts:home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.current_balance = form.cleaned_data.get('current_balance')
        form.save()

        messages.success(self.request, 'Conta criada com sucesso!')

        return super(AccountCreateView, self).form_valid(form)


class AccountUpdateView(LoginRequiredMixin, UpdateView):

    template_name = 'accounts/account-form.html'
    model = Account
    form_class = AccountForm
    success_url = reverse_lazy('accounts:home')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

        messages.success(self.request, 'Conta editada com sucesso!')

        return super(AccountUpdateView, self).form_valid(form)
