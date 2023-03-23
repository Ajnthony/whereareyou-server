from rest_framework import serializers
from .models import (Post, Category,)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['id']
        
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = [
            'id',
            'user',
            'slug',
            'is_pinned',
            'is_flagged',
            'category',
            'views',
            'likes',
            'date_created',
            'date_updated',
            'date_deleted',
            ]
        