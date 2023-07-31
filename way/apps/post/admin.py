from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Post, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active', 'num_of_posts', 'bg_color',)
    
    fieldsets = (
        (None, {'fields': ('id', 'name', 'is_active', 'num_of_posts', 'bg_color',)}),
    )
    
    ordering = ('id',)
    
    readonly_fields = ['id', 'num_of_posts', 'num_of_posts',]

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'category', 'views', 'likes', 'date_created',)
    prepopulated_fields = {'slug': ('title',)}
    
    fieldsets = (
        (_('Basic info'), {'fields': ('user', 'title', 'content', 'slug', 'category',)}),
        (_('Details'), {'fields': ('views', 'likes', 'is_flagged', 'is_deleted',)}),
        (_('Dates'), {'fields': ('date_created', 'date_updated', 'date_deleted',)}),
    )
    ordering = ('id',)
    
    readonly_fields = ['date_created', 'date_updated',]
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
