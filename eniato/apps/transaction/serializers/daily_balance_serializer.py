from rest_framework import serializers

from apps.transaction.serializers import TransactionSerializer

import calendar


class DailyBalanceSerializer(serializers.Serializer):
    reference_date = serializers.DateField()
    day_of_the_week = serializers.SerializerMethodField()
    day = serializers.SerializerMethodField()

    balance = serializers.DecimalField(max_digits=10, decimal_places=2)
    income = serializers.DecimalField(max_digits=10, decimal_places=2)
    expense = serializers.DecimalField(max_digits=10, decimal_places=2)
    credit = serializers.DecimalField(max_digits=10, decimal_places=2)

    expected_balance = serializers.DecimalField(max_digits=10, decimal_places=2)
    expected_income = serializers.DecimalField(max_digits=10, decimal_places=2)
    expected_expense = serializers.DecimalField(max_digits=10, decimal_places=2)
    expected_credit = serializers.DecimalField(max_digits=10, decimal_places=2)

    transactions = serializers.ListField(child=TransactionSerializer(), required=False)

    def get_day(self, obj):
        return obj.reference_date.day

    def get_day_of_the_week(self, obj):
        return calendar.day_name[obj.reference_date.weekday()][0:3]
