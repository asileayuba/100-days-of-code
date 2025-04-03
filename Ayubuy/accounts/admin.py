from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account, UserProfile
from django.utils.html import format_html

# Custom admin panel configuration for the Account model
class AccountAdmin(UserAdmin):
    """
    Custom admin configuration for the Account model.

    Features:
    - Displays key user details in the list view.
    - Enhances user management with clickable fields.
    - Prevents modification of auto-updated fields.
    - Orders users by newest first.
    """

    # Columns displayed in the admin list view
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')

    # Fields that can be clicked to open user details
    list_display_links = ('email', 'first_name', 'last_name')

    # Read-only fields to prevent manual modification
    readonly_fields = ('last_login', 'date_joined')

    # Orders users by newest first (descending order of date joined)
    ordering = ('-date_joined',)

    # No horizontal filters (default behavior)
    filter_horizontal = ()  

    # No additional filtering options in the admin panel
    list_filter = ()  

    # Keeps the default field arrangement (does not modify fieldsets)
    fieldsets = ()  
    
    
class UserProfileAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="30" style="border-radius: 50%;">'.format(object.profile_picture.url))
    thumbnail.short_description = 'Profile Picture'
    list_display = ('thumbnail', 'user', 'city', 'state', 'country')

# Register the Account model with the custom admin panel configuration
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Account, AccountAdmin)
