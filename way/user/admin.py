from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['id', 'email', 'first_name', 'last_name', 'display_name']
    
    fieldsets = (
        (_('Basic info'), {'fields': ('first_name', 'last_name', 'display_name', 'email',)}),
        (_('Details'), {'fields': ('profile_url', 'bio',)}),
        (_('Address'), {'fields': ('address_line_1', 'address_line_2', 'city', 'state', 'country', 'zip_code',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_moderator', 'is_staff', 'is_superuser',)}),
        (_('Important dates'), {'fields': ('date_created','date_updated', 'last_login',)}),
    )
    readonly_fields = ['last_login']
    
    # this is for creating a new user in admin page
    add_fieldsets = (
        (_('Password'), {
            'classes': ('wide',),
            'fields': {
                'email',
                'password1',
                'password2',
            }
        }),
    )

admin.site.register(User, UserAdmin)