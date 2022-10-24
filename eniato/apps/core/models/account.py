from django.db import models
from lib.framework.models.base_model import BaseModel

from django.contrib.auth import get_user_model

User = get_user_model()


class Account(BaseModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Usuário')
    name = models.CharField(max_length=255, verbose_name='Conta')
    opening_balance = models.DecimalField(max_digits=10, decimal_places=2, null=True, verbose_name='Saldo inicial')
    # tipo da conta
    # color
    # padrão ?
    # 

    class Meta:
        verbose_name = 'Conta'
        verbose_name_plural = 'Contas'
