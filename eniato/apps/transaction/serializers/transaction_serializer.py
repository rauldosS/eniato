from rest_framework import serializers

from apps.accounts.serializers import AccountSerializer
from apps.category.serializers import CategorySerializer

from apps.transaction.constants import TransactionType


class TransactionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    category = CategorySerializer()
    account = AccountSerializer(required=False, allow_null=True)
    #credit_card
    #store
    #tag
    #recurrence
    #installment
    value = serializers.DecimalField(decimal_places=2, max_digits=10)
    description = serializers.CharField()
    transaction_date = serializers.DateField()
    transaction_type = serializers.CharField()
    status = serializers.BooleanField()
    ignore = serializers.BooleanField()
    is_expense = serializers.SerializerMethodField()
    # file
    observation = serializers.CharField()

    def get_is_expense(self, obj):
        if (obj.transaction_type == TransactionType.INCOME.value) or (obj.transaction_type == TransactionType.INCOMING_TRANSFER.value):
            return False
        return True
