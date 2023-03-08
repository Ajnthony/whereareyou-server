from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from .models import Animal, Tag

class AnimalAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['id', 'name', 'size','gender','is_found', 'views', 'likes', 'date_created']
    
    fieldsets = (
        (_('Basic info'), {'fields': ('name',)}),
        (_('Details'), {'fields':('owner','size','gender','description','species','is_found','last_seen_date','last_seen_location',)}),
        (_('Image'), {'fields':('image',)}),
        (_('Meta'), {'fields':('views','likes',)}),
        (_('Dates'), {'fields': ('date_created','date_updated',)}),
    )
    
class TagAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['id', 'name']
    
    fieldsets = (
        (_('Basic info'), {'fields': ('name',)}),
        (_('Colours'), {'fields': ('red', 'green', 'blue',)}),
        (_('Dates'), {'fields':('date_created', 'date_updated',)}),
    )

admin.site.register(Animal, AnimalAdmin)
admin.site.register(Tag, TagAdmin)