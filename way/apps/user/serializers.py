from django.contrib.auth import (
    get_user_model,
    authenticate,
)
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            'id',
            'first_name',
            'last_name',
            'display_name',
            'email',
            'password',
            'is_active',
            'is_moderator',
            'is_admin',
            'is_staff',
            'is_superuser',
            ]
        extra_kwargs = {'password': {'write_only': True, 'min_length': 6}}

        
    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)
    
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)
        
        if password:
            user.set_password(password)
        
        user.save()    
        return user