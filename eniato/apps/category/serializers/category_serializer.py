from rest_framework import serializers
from lib.users.serializers.user_serializer import UserSerializer


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    user = UserSerializer()
    category_type = serializers.CharField()
    name = serializers.CharField()
    color = serializers.CharField()
    icon = serializers.CharField()
    default = serializers.BooleanField()
