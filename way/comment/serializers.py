from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = [
            'id',
            'user',
            'post',
            'is_deleted',
            'is_flagged',
            'likes',
            'date_created',
            'date_updated',
            'date_deleted',
            ]
        