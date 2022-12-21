from rest_framework import serializers

from apps.accounts.serializers import AccountSerializer
from apps.category.serializers import CategorySerializer
from apps.transaction.serializers.recurrence_serializer import RecurrenceSerializer

from apps.transaction.constants import TransactionType

from apps.transaction.constants import TRANSACTION_TYPE_DISPLAY_NAME


class TransactionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    category = CategorySerializer()
    account = AccountSerializer(required=False, allow_null=True)
    recurrence = RecurrenceSerializer(required=False, allow_null=True)
    value = serializers.DecimalField(decimal_places=2, max_digits=10)
    description = serializers.CharField()
    transaction_date = serializers.DateField()
    transaction_type = serializers.CharField()
    transaction_type_display_name = serializers.SerializerMethodField()
    installment = serializers.IntegerField()
    status = serializers.BooleanField()
    is_expense = serializers.SerializerMethodField()
    observation = serializers.CharField()

    def get_transaction_type_display_name(self, obj):
        return dict(TRANSACTION_TYPE_DISPLAY_NAME)[obj.transaction_type]

    def get_is_expense(self, obj):
        if (obj.transaction_type == TransactionType.INCOME.value) or (obj.transaction_type == TransactionType.INCOMING_TRANSFER.value):
            return False
        return True
