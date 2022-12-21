from rest_framework import serializers
from lib.users.serializers.user_serializer import UserSerializer

from .financial_institution_serializer import FinancialInstitutionSerializer

from apps.accounts.constants import ACCOUNT_TYPE_DISPLAY_NAME


class AccountSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    user = UserSerializer()
    financial_institution = FinancialInstitutionSerializer()
    opening_balance = serializers.DecimalField(decimal_places=2, max_digits=10)
    current_balance = serializers.DecimalField(decimal_places=2, max_digits=10)
    description = serializers.CharField()
    account_type = serializers.CharField()
    display_account_type = serializers.SerializerMethodField()
    color = serializers.CharField()
    default = serializers.BooleanField()
    active = serializers.BooleanField()

    def get_display_account_type(self, obj):
        return dict(ACCOUNT_TYPE_DISPLAY_NAME)[obj.account_type]
