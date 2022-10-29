from rest_framework import serializers
from user.models import PostUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostUser
        fields = ['id', 'username', 'email',
                  'first_name', 'last_name', 'is_active']