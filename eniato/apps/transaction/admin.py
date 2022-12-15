from django.contrib import admin

from apps.transaction.models.transaction import Transaction
from apps.transaction.models.daily_balance import DailyBalance

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'description', 'transaction_date', 'transaction_type', 'value')
    ordering = ('transaction_date',)

@admin.register(DailyBalance)
class DailyBalanceAdmin(admin.ModelAdmin):
    # filter_horizontal = ('transactions',)
    list_display = (
        'id',
        'reference_date',
        'balance',
        'income',
        'expense',
        'credit',
        'expected_balance',
        'expected_income',
        'expected_expense',
        'expected_credit'
    )
    ordering = ('reference_date',)
