from django.db import models
from lib.framework.models.base_model import BaseModel

from apps.core.constants import FinancialInstitutionType


class FinancialInstitution(BaseModel):
    code = models.CharField(max_length=3, verbose_name='Código')
    name = models.CharField(max_length=255, verbose_name='Nome')
    icon = models.ImageField(upload_to='financial_institution/', verbose_name='Ícone')

    class Meta:
        verbose_name = 'Instituição Financeira'
        verbose_name_plural = 'Instituições Financeiras'
