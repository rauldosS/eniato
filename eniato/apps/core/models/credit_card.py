from django.db import models
from lib.framework.models.base_model import BaseModel

from apps.core.models.account import Account
from apps.core.models.flag import Flag



class CreditCard(BaseModel):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='Cartão')
    flag = models.ForeignKey(Flag, on_delete=models.CASCADE, related_name='Bandeira')
    limit = models.DecimalField(verbose_name='Limite', max_digits=10, decimal_places=2, null=True)
    description = models.CharField(verbose_name='Descrição', max_length=255)
    default = models.BooleanField('Padrão', default=False)
    invoice_closing = models.DateField(blank=False, null=False, verbose_name='Dia de fechamento')
    invoice_expiration = models.DateField(blank=False, null=False, verbose_name='Dia do vencimento')

    class Meta:
        verbose_name = 'Cartão de Crédito'
        verbose_name_plural = 'Cartões de Crédito'
