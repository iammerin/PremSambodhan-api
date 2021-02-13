from rest_framework import serializers
from .models import User, UserProfile, Message


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)
    confirm_password = serializers.CharField(max_length=255)

  
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)


class UserDataSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)
    
    class Meta:
        model = UserProfile
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
    receiver = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'message', 'timestamp']

class MessagingSerializer(serializers.Serializer):
    reciever_id = serializers.CharField(max_length=255)
    message = serializers.CharField()
    

class UpdateProfileSerializers(serializers.Serializer):
    full_name = serializers.CharField(max_length=255,required=False)
    address = serializers.CharField(max_length=255,required=False)
    contact_number = serializers.CharField(max_length=255,required=False)
    instagram_id = serializers.CharField(max_length=255,required=False)
    facebook_id = serializers.CharField(max_length=255,required=False)
    gender = serializers.CharField(max_length=255,required=False)
    profile_image = serializers.ImageField(required=False)
