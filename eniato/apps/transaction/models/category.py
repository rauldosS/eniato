from django.db import models
from lib.framework.models.base_model import BaseModel

from django.contrib.auth import get_user_model

from apps.core.constants import TransactionType, Color

User = get_user_model()


class Category(BaseModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Usuário')
    category_type = models.CharField(
        choices=[(transaction_type.value, transaction_type.name) for transaction_type in TransactionType],
        max_length=50,
        verbose_name='Tipo'
    )
    name = models.CharField(verbose_name='Nome', max_length=255)
    color = models.CharField(
        choices=[(color.value, color.name) for color in Color],
        max_length=50,
        verbose_name='Cor da Categoria'
    )
    icon = models.ImageField(upload_to='categories/', verbose_name='Ícone')
    default = models.BooleanField(default=False, verbose_name='Padrão do Sistema')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
