from django.db import models
from django.conf import settings
from django.utils.text import slugify
from utils.helpers import generate_hexcode

class Category(models.Model):
    # basic info
    name = models.CharField(max_length=50)
    
    # details
    is_active = models.BooleanField(default=True)
    num_of_posts = models.IntegerField(default=0)
    bg_color = models.CharField(max_length=6, default=None, null=True, blank=True)
    
    def save(self, *args, **kwargs):
        created = not self.pk
        
        if created:
            self.bg_color = generate_hexcode()
        
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Post(models.Model):
    # relations
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    
    # basic info
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=2000)
    slug = models.SlugField(unique=True, unique_for_date='date_created')
    
    # details
    is_pinned = models.BooleanField(default=False)
    is_flagged = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    # dates
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_deleted = models.DateTimeField(default=None, null=True, blank=True)
    
    
    def save(self, *args, **kwargs):
        created = not self.pk
        
        if created and not self.slug:
            self.slug = slugify(self.title)
        
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title