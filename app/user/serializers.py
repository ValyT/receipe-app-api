"""Serializers for user API view"""
from django.contrib.auth import get_user_model

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializers):
    """Serializers for user object"""

    class Meta:
        mode=get_user_model()
        fields=['email','password','name']
        extra_kwargs = {'password': {'write__only': True, 'min_length': 5}}

    def create(self, validated_data):
        """Create and return user with encrypted password"""
        return get_user_model().objects.create_user(**validated_data)
