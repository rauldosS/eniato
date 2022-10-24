from django.db import models
from lib.framework.models.base_model import BaseModel

from apps.core.constants import Color


class FinancialInstitution(BaseModel):
    name = models.CharField(max_length=255, verbose_name='Nome')
    icon = models.ImageField(upload_to='stores/', verbose_name='Ícone')
    color = models.CharField(
        choices=[(color.value, color.name) for color in Color],
        max_length=50,
        verbose_name='Cor'
    )

    class Meta:
        verbose_name = 'Loja'
        verbose_name_plural = 'Lojas'
