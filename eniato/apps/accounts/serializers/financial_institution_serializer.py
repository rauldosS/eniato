from rest_framework import serializers


class FinancialInstitutionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    code = serializers.CharField()
    name = serializers.CharField()
    logo = serializers.URLField()
