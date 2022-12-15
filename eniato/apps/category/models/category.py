from django.db import models
from lib.framework.models.base_model import BaseModel

from django.contrib.auth import get_user_model

from apps.core.constants import Color, Icon
from apps.category.constants import CategoryType

User = get_user_model()


class Category(BaseModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Usuário')
    category_type = models.CharField(
        choices=[(category_type.value, category_type.name) for category_type in CategoryType],
        max_length=50,
        verbose_name='Tipo da categoria'
    )
    name = models.CharField(verbose_name='Nome', max_length=255)
    color = models.CharField(
        choices=[(color.value, color.name) for color in Color],
        max_length=50,
        verbose_name='Cor da Categoria'
    )
    icon = models.CharField(
        choices=[(icon.value, icon.name) for icon in Icon],
        max_length=50,
        verbose_name='Ícone'
    )
    default = models.BooleanField(default=False, verbose_name='Padrão do Sistema')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
