from django.db import models
from lib.framework.models.base_model import BaseModel


class FinancialInstitution(BaseModel):
    code = models.CharField(max_length=3, verbose_name='Código')
    name = models.CharField(max_length=255, verbose_name='Nome')
    logo = models.ImageField(upload_to='financial_institution/', verbose_name='Logo', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Instituição Financeira'
        verbose_name_plural = 'Instituições Financeiras'
