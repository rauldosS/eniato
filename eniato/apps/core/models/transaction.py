from django.db import models
from lib.framework.models.base_model import BaseModel

from apps.core.models.recurrence import Recurrence
from apps.core.models.category import Category

from apps.core.constants import PaymentMethodType


class Transaction(BaseModel):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='Loja')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='Categoria')
    recurrence = models.ForeignKey(Recurrence, on_delete=models.CASCADE, related_name='Recorrência')

    date = models.DateField(blank=False, null=False, verbose_name='Data')
    payment_method = models.CharField(
        choices=[(card_type.value, card_type.name) for card_type in PaymentMethodType],
        max_length=50,
        verbose_name='Método de Pagamento'
    )
    
    value = models.DecimalField(verbose_name='Valor', max_digits=10, decimal_places=2, null=True)
    payment_voucher = models.FileField(uppload_to='uploads/payments_voucher/%Y/%m/%d/')
    status = models.BooleanField(verbose_name='Situação', default=False)
    observation = models.TextField(verbose_name='Observação', null=True, blank=True)

    class Meta:
        verbose_name = 'Transação'
        verbose_name_plural = 'Transações'
