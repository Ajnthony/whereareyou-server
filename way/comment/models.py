from django.db import models
from post.models import Post
from django.conf import settings

class Comment(models.Model):
    # basic fields
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    post = models.ForeignKey(Post, on_delete=models.PROTECT)
    content = models.TextField(max_length=1000)
    
    # details
    is_deleted = models.BooleanField(default=False)
    is_flagged = models.BooleanField(default=False)
    likes = models.IntegerField(default=0)
    
    # dates
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_deleted = models.DateTimeField(default=None, null=True, blank=True)
    
    def __str__(self):
        return f'Comment for post {self.post} by {self.user}'