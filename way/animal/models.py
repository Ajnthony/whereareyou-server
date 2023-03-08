import random
from django.db import models
from django.utils import timezone
from django.conf import settings

class Animal(models.Model):
    animal_types = ['dog','cat','turtle','bird','snake','lizard','animal','pet']
    query = random.choice(animal_types)
    
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    size = models.CharField(max_length=3) # XXL at most...
    last_seen_date = models.DateTimeField(default=timezone.now)
    last_seen_location = models.CharField(max_length=2, default='CA') # CA, NY, OR, ...        
    gender = models.CharField(max_length=6) # 'Female' would be the longest
    description = models.TextField(max_length=255, null=True)
    species = models.CharField(max_length=20)
    is_found = models.BooleanField(default=False)
    image = models.ImageField(blank=True, default=f'https://source.unsplash.com/random/?{query}')
    tags = models.ManyToManyField('Tag')
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(default=timezone.now)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.name
    
class Tag(models.Model):
    # to be used as rgb value for background in the frontend
    red_value = random.choice(range(0, 256)) # between 0 and 255
    green_value = random.choice(range(0, 256))
    blue_value = random.choice(range(0, 256))
    
    name = models.CharField(max_length=50)
    red = models.IntegerField(default=red_value)
    green = models.IntegerField(default=green_value)
    blue = models.IntegerField(default=blue_value)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(default=timezone.now)
    
    def __str__(self) -> str:
        return self.name