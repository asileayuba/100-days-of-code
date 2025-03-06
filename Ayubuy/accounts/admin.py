from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

# Register your models here.

class AccountAdmin(UserAdmin):
    """
    Custom admin configuration for the Account model.

    Features:
    - Displays user details including email, name, username, last login, date joined, and active status.
    - Customizes the admin panel view for better user management.
    """
    
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')  # Columns shown in the admin list view
    
    filter_horizontal = ()  # No horizontal filters applied
    list_filter = ()  # No additional filtering options applied
    fieldsets = ()  # Keeps the default field arrangement

# Registers the Account model with the custom admin configuration
admin.site.register(Account, AccountAdmin)
