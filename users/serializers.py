from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UsersDetails

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'email', 'password', 'first_name', 'last_name']
        

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersDetails
        fields = ['country', 'phone_number', 'ci','user_role', 'profile_image', 'address']