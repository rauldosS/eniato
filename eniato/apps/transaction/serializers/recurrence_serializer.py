from rest_framework import serializers


class RecurrenceSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    fixed = serializers.BooleanField()
    repeat_amount = serializers.IntegerField()
    repeat_period = serializers.CharField()
