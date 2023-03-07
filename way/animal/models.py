from django.db import models
from django.utils import timezone
from django.conf import settings

class Animal(models.Model):
    # owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    size = models.CharField(max_length=3) # XXL at most...
    last_seen = {
        'datetime': models.DateTimeField(),
        'location': models.CharField(max_length=2) # CA, NY, OR, ...
        }
    gender = models.CharField(max_length=6) # 'Female' would be the longest
    description = models.TextField(max_length=255, null=True)
    species = models.CharField(max_length=20)
    is_found = models.BooleanField(default=False)
    image = models.ImageField(null=True, default='')
    tags = models.ManyToManyField('Tag')
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(default=timezone.now)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=50)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name