from django.db import models
from lib.framework.models.base_model import BaseModel

from django.contrib.auth import get_user_model

from apps.accounts.models.account import Account
from apps.credit_card.models.flag import Flag

User = get_user_model()


class CreditCard(BaseModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Usuário')
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='Cartão')
    flag = models.ForeignKey(Flag, on_delete=models.CASCADE, related_name='Bandeira')

    limit = models.DecimalField(verbose_name='Limite', max_digits=10, decimal_places=2, null=True)
    invoice_closing = models.DateField(verbose_name='Dia de fechamento')
    invoice_expiration = models.DateField(verbose_name='Dia do vencimento')

    description = models.CharField(verbose_name='Descrição', max_length=255)
    default = models.BooleanField(verbose_name='Padrão', default=False)

    class Meta:
        verbose_name = 'Cartão de Crédito'
        verbose_name_plural = 'Cartões de Crédito'
