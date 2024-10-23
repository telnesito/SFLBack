from .models import Users
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id','username', 'email', 'password', 'firstname', 'lastname', 'created_at']
        read_only_fields=['created_at']