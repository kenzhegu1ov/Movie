from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError


class UserCreateSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate_username(self, username):
        try:
            User.objects.get(username=username)
            raise ValidationError('User already exists')
        except User.DoesNotExist:
            return username
