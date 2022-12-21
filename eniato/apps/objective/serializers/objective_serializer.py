from rest_framework import serializers
from lib.users.serializers.user_serializer import UserSerializer

from apps.objective.constants import STATUS_DISPLAY_NAME


class ObjectiveSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    user = UserSerializer()
    value = serializers.DecimalField(decimal_places=2, max_digits=10)
    balance = serializers.DecimalField(decimal_places=2, max_digits=10)
    objective_date = serializers.DateField()
    name = serializers.CharField()
    color = serializers.CharField()
    icon = serializers.CharField()
    status = serializers.CharField()
    status_display_name = serializers.SerializerMethodField()
    description = serializers.CharField()

    def get_status_display_name(self, obj):
        return dict(STATUS_DISPLAY_NAME)[obj.status]
