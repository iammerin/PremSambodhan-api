from rest_framework import serializers
from .models import UserProfile
from .models import User


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)
    confirm_password = serializers.CharField(max_length=255)

  
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)

class UserDataSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(read_only=True)
    class Meta:
        model = UserProfile
        fields = '__all__'