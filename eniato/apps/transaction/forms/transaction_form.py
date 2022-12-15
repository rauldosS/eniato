from django import forms

from apps.transaction.models.transaction import Transaction
from apps.category.models.category import Category

from apps.accounts.repositories import AccountRepository
from apps.category.repositories import CategoryRepository

from apps.core.constants import Color
from apps.transaction.constants import (
    TransactionType,
    TRANSACTION_TYPE_BY_DISPLAY_NAME,
    CATEGORY_TYPE_FOR_TRANSACTION_TYPE
)


class TransactionForm(forms.ModelForm):
    # category
    # account
    # credit_card
    # store
    # tag
    # recurrence

    # installment

    value = forms.DecimalField(required=False)
    description = forms.CharField(initial='')
    transaction_type = forms.CharField(required=False)

    # file
    observation = forms.CharField(initial='', required=False)

    def __init__(self, *args, **kwargs):
        account_repository = AccountRepository()
        category_repository = CategoryRepository()

        self.request = kwargs.pop('request')
        self.kwargs = kwargs.pop('kwargs')

        self.kwargs['transaction_type'] = dict(TRANSACTION_TYPE_BY_DISPLAY_NAME)[self.kwargs.get('transaction_type')]

        super(TransactionForm, self).__init__(*args, **kwargs)

        categories = category_repository.get_by_type(self.request.user, dict(CATEGORY_TYPE_FOR_TRANSACTION_TYPE)[self.kwargs['transaction_type']])
        accounts = account_repository.get_model_by_user(self.request.user)

        self.fields['category'].queryset = categories
        self.fields['account'].queryset = accounts

    class Meta:
        model = Transaction
        fields = (
            'category',
            'account',
            'installment',
            'value',
            'description',
            'transaction_date',
            'transaction_type',
            'status',
            'ignore',
            'observation',
        )

    def clean_transaction_type(self):
        return self.kwargs['transaction_type']

    def clean(self):
        return super(TransactionForm, self).clean()
