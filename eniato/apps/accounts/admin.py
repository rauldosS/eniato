from django.contrib import admin

from apps.accounts.models.financial_institution import FinancialInstitution
from apps.accounts.models.account import Account

@admin.register(FinancialInstitution)
class FinancialInstitutionAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name')

admin.site.register(Account)
