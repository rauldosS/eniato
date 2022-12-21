from django.contrib import admin

from apps.transaction.models.transaction import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'description', 'transaction_date', 'transaction_type', 'value')
    ordering = ('transaction_date',)
