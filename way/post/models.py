from django.db import models
from django.conf import settings
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    # basic fields
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=2000)
    slug = models.SlugField(unique=True, unique_for_date='date_created')
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
        if not self.slug:
            self.slug = slugify(self.title)
            super(Post, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title