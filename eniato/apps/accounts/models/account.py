from django.db import models
from lib.framework.models.base_model import BaseModel

from django.contrib.auth import get_user_model

from apps.core.constants import FinancialInstitutionType, Color
from apps.accounts.models.financial_institution import FinancialInstitution

User = get_user_model()


class Account(BaseModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Usuário')
    financial_institution = models.ForeignKey(FinancialInstitution, on_delete=models.CASCADE, verbose_name='Instituição Financeira')
    opening_balance = models.DecimalField(max_digits=10, decimal_places=2, null=True, verbose_name='Saldo inicial')
    description = models.CharField(max_length=255, verbose_name='Descrição')
    account_type = models.CharField(
        choices=[(account_type.value, account_type.name) for account_type in FinancialInstitutionType],
        max_length=50,
        verbose_name='Cor'
    )
    color = models.CharField(
        choices=[(color.value, color.name) for color in Color],
        max_length=50,
        verbose_name='Cor'
    )
    default = models.BooleanField(verbose_name='Conta Padrão', default=False)

    class Meta:
        verbose_name = 'Conta'
        verbose_name_plural = 'Contas'
