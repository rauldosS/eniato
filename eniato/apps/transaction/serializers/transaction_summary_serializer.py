from rest_framework import serializers

from apps.transaction.serializers import DailyBalanceSerializer

class TransactionSummarySerializer(serializers.Serializer):
    period = serializers.CharField()
    daily_balances = serializers.ListField(child=DailyBalanceSerializer(), required=False)
    period_balance = serializers.DecimalField(decimal_places=2, max_digits=10)
    expected_period_balance = serializers.DecimalField(decimal_places=2, max_digits=10)
    total_income = serializers.DecimalField(decimal_places=2, max_digits=10)
    total_expense = serializers.DecimalField(decimal_places=2, max_digits=10)
    balance = serializers.DecimalField(decimal_places=2, max_digits=10)
    total_expected_income = serializers.DecimalField(decimal_places=2, max_digits=10)
    total_expected_expense = serializers.DecimalField(decimal_places=2, max_digits=10)
    expected_balance = serializers.DecimalField(decimal_places=2, max_digits=10)
