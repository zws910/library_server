from rest_framework import serializers

from .models import User


class CurrentUserSerializer(serializers.ModelSerializer):
    """
    用户信息
    """
    class Meta:
        model = User
        fields = ('id', 'username', 'mobile', 'email')