from django import forms

from apps.accounts.models.account import Account
from apps.accounts.models.financial_institution import FinancialInstitution

from apps.accounts.constants import (
    ACCOUNT_TYPES,
    ACCOUNT_TYPE_CHECKING_ACCOUNT as CHECKING_ACCOUNT,
    ACCOUNT_TYPE_MONEY as MONEY,
    ACCOUNT_TYPE_SAVINGS as SAVINGS,
    ACCOUNT_TYPE_INVESTMENTS as INVESTMENTS,
    ACCOUNT_TYPE_OTHERS as OTHERS,
)
from apps.core.constants import Color


class AccountForm(forms.ModelForm):
    description = forms.CharField(initial='')
    current_balance = forms.DecimalField(required=False)
    opening_balance = forms.CharField(required=False)
    color = forms.ChoiceField(
        choices=[(color.value, color.name) for color in Color],
        required=True,
        initial=Color.BLUE.value
    )
    account_type = forms.ChoiceField(choices=[
        (CHECKING_ACCOUNT, ACCOUNT_TYPES[CHECKING_ACCOUNT]),
        (MONEY, ACCOUNT_TYPES[MONEY]),
        (SAVINGS, ACCOUNT_TYPES[SAVINGS]),
        (INVESTMENTS, ACCOUNT_TYPES[INVESTMENTS]),
        (OTHERS, ACCOUNT_TYPES[OTHERS]),
    ])

    def __init__(self, *args, **kwargs):
        super(AccountForm, self).__init__(*args, **kwargs)
        self.fields['opening_balance'].disabled = not kwargs.get('instance') is None

    class Meta:
        model = Account
        fields = ('financial_institution', 'description', 'opening_balance', 'account_type', 'default', 'color')

        widgets = {
            'color': forms.HiddenInput(),
            'current_balance': forms.HiddenInput(),
        }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['opening_balance'].widget.attrs.update({
    #         'class': 'currency-mask-without-prefix',
    #         'placeholder': '0,00',
    #     })

    def clean_current_balance(self):
        current_balance = None
        if not self.cleaned_data.get('current_balance'):
            current_balance = self.cleaned_data.get('opening_balance')
        return current_balance

    def clean(self):
        return super(AccountForm, self).clean()

"""class AccountForm(forms.Form):
    financial_institution = forms.ModelChoiceField(queryset=FinancialInstitution.objects.all(), required=True)
    opening_balance = forms.BooleanField(required=True)
    description = forms.CharField(required=True)

    account_type = forms.ChoiceField(choices=[
        (CHECKING_ACCOUNT, ACCOUNT_TYPES[CHECKING_ACCOUNT]),
        (MONEY, ACCOUNT_TYPES[MONEY]),
        (SAVINGS, ACCOUNT_TYPES[SAVINGS]),
        (INVESTMENTS, ACCOUNT_TYPES[INVESTMENTS]),
        (OTHERS, ACCOUNT_TYPES[OTHERS]),
    ])

    default = forms.BooleanField(required=False)
    color = forms.CharField(widget=forms.HiddenInput(), required=False)

    def clean_financial_institution(self):
        financial_institution = None
        if self.cleaned_data.get('financial_institution'):
            financial_institution = self.cleaned_data['financial_institution'].id
        return financial_institution

    def clean(self):
        return super(AccountForm, self).clean()

    # class Meta:
    #     model = Account
    #     fields = (
    #         'financial_institution',
    #         'opening_balance',
    #         'description',
    #         'account_type',
    #         'color',
    #         'default'
    #     )

    #     widgets = {
    #         'user': forms.HiddenInput(),
    #         'color': forms.HiddenInput(),
    #     }

    #     user_profile_codes = forms.MultipleChoiceField(choices=[
    #         (ADMINISTRATIVE, CAMPAIGN_TEAM_USER_PROFILES[ADMINISTRATIVE]),
    #         (EXAMINER, CAMPAIGN_TEAM_USER_PROFILES[EXAMINER]),
    #         (COORDINATOR, CAMPAIGN_TEAM_USER_PROFILES[COORDINATOR])
    #     ])
"""