from django.db import models
from lib.framework.models.base_model import BaseModel

from apps.core.constants import TransactionType, Color


class Category(BaseModel):
    category_type = models.CharField(
        choices=[(transaction_type.value, transaction_type.name) for transaction_type in TransactionType],
        max_length=50,
        verbose_name='Categoria'
    )
    name = models.CharField(verbose_name='Nome', max_length=255)
    color = models.CharField(
        choices=[(color.value, color.name) for color in Color],
        max_length=50,
        verbose_name='Cor'
    )
    icon = models.ImageField(upload_to='categories/', verbose_name='Ícone')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
