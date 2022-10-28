from django.db import models
from lib.framework.models.base_model import BaseModel

from apps.transaction.models.category import Category
from apps.transaction.models.store import Store
from apps.transaction.models.tag import Tag

from apps.credit_card.models.credit_card import CreditCard
from apps.accounts.models.account import Account

from apps.core.constants import PaymentMethodType, TransactionType


class Transaction(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='Categoria')
    credit_card = models.ForeignKey(CreditCard, on_delete=models.CASCADE, related_name='Cartão de crédito', null=True, blank=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='Cartão de crédito', null=True, blank=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='Loja', null=True, blank=True)
    tag = models.ManyToManyField(Tag, on_delete=models.CASCADE, related_name='Tags', null=True, blank=True)

    value = models.DecimalField(verbose_name='Valor', max_digits=10, decimal_places=2, default=0.00)
    transaction_date = models.DateField(verbose_name='Data', blank=False, null=False)
    transaction_type = models.CharField(
        choices=[(transaction_type.value, transaction_type.name) for transaction_type in TransactionType],
        max_length=50,
        verbose_name='Tipo de transação'
    )

    status = models.BooleanField(verbose_name='Situação', default=False)
    ignore = models.BooleanField(verbose_name='Ignorar transação', default=False)
    calculate = models.BooleanField(verbose_name='Calcular', default=False)

    file = models.FileField(verbose_name='Arquivo', uppload_to='uploads/transitions/files/%Y/%m/%d/')
    observation = models.TextField(verbose_name='Observação', null=True, blank=True)

    # recurrence = models.ForeignKey(Recurrence, on_delete=models.CASCADE, related_name='Recorrência', null=True, blank=True)
    fixed = models.BooleanField(verbose_name='Fixa', default=False)

    class Meta:
        verbose_name = 'Transação'
        verbose_name_plural = 'Transações'
