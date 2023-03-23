from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Comment



class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'post', 'date_created',)
    
    fieldsets = (
        (_('Basic info'), {'fields': ('user', 'post', 'content', 'likes',)}),
        (_('Details'), {'fields': ('is_flagged', 'is_deleted',)}),
        (_('Dates'), {'fields': ('date_created', 'date_updated', 'date_deleted',)}),
    )
    
    ordering = ('id',)
    
    readonly_fields = ['date_created', 'date_updated',]
    
admin.site.register(Comment, CommentAdmin)
