from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Post, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active',)
    
    fieldsets = (
        (None, {'fields': ('name', 'is_active',)}),
    )
    
    ordering = ('id',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'category', 'views', 'likes', 'date_created',)
    prepopulated_fields = {'slug': ('title',)}
    
    fieldsets = (
        (_('Basic info'), {'fields': ('user', 'title', 'content', 'slug', 'category', 'views', 'likes',)}),
        (_('Details'), {'fields': ('is_flagged', 'is_deleted',)}),
        (_('Dates'), {'fields': ('date_created', 'date_updated', 'date_deleted',)}),
    )
    ordering = ('id',)
    
    readonly_fields = ['date_created', 'date_updated',]
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
