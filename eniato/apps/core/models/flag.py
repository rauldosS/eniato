from django.db import models
from lib.framework.models.base_model import BaseModel

from apps.core.models.account import Account
from apps.core.models.bank import Bank


class Flag(BaseModel):
    name = models.CharField(verbose_name='Nome', max_length=255)
    icon = models.ImageField(upload_to='categories/', verbose_name='Ícone')

    class Meta:
        verbose_name = 'Bandeira'
        verbose_name_plural = 'Bandeiras'