from django.db import models
from lib.framework.models.base_model import BaseModel
from django.contrib.auth import get_user_model

from apps.core.constants import Color, Icon
from apps.objective.constants import Status

User = get_user_model()


class Objective(BaseModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Usuário')
    value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor do objetivo')
    balance = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Saldo')
    objective_date = models.DateField(verbose_name='Data final do objetivo', blank=False, null=False)
    name = models.CharField(max_length=55, verbose_name='Nome')
    color = models.CharField(
        choices=[(color.value, color.name) for color in Color],
        max_length=50,
        verbose_name='Cor da conta'
    )
    icon = models.CharField(
        choices=[(icon.value, icon.name) for icon in Icon],
        max_length=50,
        verbose_name='Ícone'
    )
    status = models.CharField(
        choices=[(status.value, status.name) for status in Status],
        default='active',
        max_length=50,
        verbose_name='Status'
    )
    description = models.CharField(max_length=255, verbose_name='Descrição', default='')
