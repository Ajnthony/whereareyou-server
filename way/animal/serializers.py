from rest_framework import serializers
from .models import (
    Animal,
    Tag,
)

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
        read_only_fields = ['id']
        # fields = ['id', 'name', 'animal']
        
class AnimalSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, required=False)
    
    class Meta:
        model = Animal
        # fields = '__all__'
        fields = [
            'id',
            'user',
            'name',
            'size',
            'last_seen_date',
            'last_seen_location',
            'gender',
            'description',
            'species',
            'is_found',
            'image',
            'tags',
            'date_created',
            'date_updated',
            'views',
            'likes',
        ]
        read_only_fields = [
            'id',
            'user',
            'date_created',
            'date_updated',
            'views',
            'likes'
            ]
        
    def _get_or_create_tags(self, tags, animal):
        
        for tag in tags:
            tag_obj, created = Tag.objects.get_or_create(
                animal=animal,
                **tag
            )
            animal.tags.add(tag_obj)
            
    def create(self, validated_data):
        tags = validated_data.pop('tags', [])
        animal = Animal.objects.create(**validated_data)
        self._get_or_create_tags(tags, animal)
        
        return animal
    
    def update(self, instance, validated_data):
        tags = validated_data.pop('tags', None)
        
        if tags is not None:
            instance.tags.clear()
            self._get_or_create_tags(tags, instance)
            
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
            
        instance.save()
        return instance
    
class AnimalDetailSerializer(AnimalSerializer):
    class Meta(AnimalSerializer.Meta):
        fields = AnimalSerializer.Meta.fields + ['size', 'last_seen_date', 'last_seen_location', 'gender']