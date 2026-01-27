from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=42)
    password = serializers.CharField(write_only=True, min_length=8)
    email = serializers.EmailField()

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Ce nom d'utilisateur est déjà pris")
        return value
