from django.db import models
from lib.framework.models.base_model import BaseModel

from apps.category.models import Category
from apps.transaction.models.daily_balance import DailyBalance
from apps.transaction.models.store import Store
from apps.transaction.models.tag import Tag
from apps.transaction.models.recurrence import Recurrence

from apps.accounts.models.account import Account

from apps.transaction.constants import TransactionType
from django.contrib.auth import get_user_model

User = get_user_model()


class Transaction(BaseModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Usuário')
    daily_balance = models.ForeignKey(DailyBalance, on_delete=models.CASCADE, verbose_name='Balanço diário', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_transaction')

    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='account_transaction', null=True, blank=True)
    destination_account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='destination_account_transaction', null=True, blank=True)

    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='store_transaction', null=True, blank=True)
    tag = models.ManyToManyField(Tag, related_name='tags_transaction', blank=True)
    recurrence = models.ForeignKey(Recurrence, on_delete=models.CASCADE, related_name='recorrence_transaction', null=True, blank=True)

    installment = models.IntegerField(verbose_name='Parcela', null=True, blank=True)

    value = models.DecimalField(verbose_name='Valor', max_digits=10, decimal_places=2, default=0.00)
    description = models.CharField(verbose_name='Descrição', max_length=255)
    transaction_date = models.DateField(verbose_name='Data', blank=False, null=False)
    transaction_type = models.CharField(
        choices=[(transaction_type.value, transaction_type.name) for transaction_type in TransactionType],
        max_length=50,
        verbose_name='Tipo de transação'
    )

    status = models.BooleanField(verbose_name='Situação', default=False)
    ignore = models.BooleanField(verbose_name='Ignorar transação', default=False)

    file = models.FileField(verbose_name='Arquivo', upload_to='uploads/transitions/%Y/%m/%d/', null=True, blank=True)
    observation = models.TextField(verbose_name='Observação', null=True, blank=True)

    class Meta:
        verbose_name = 'Transação'
        verbose_name_plural = 'Transações'
