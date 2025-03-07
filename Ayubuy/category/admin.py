from django.contrib import admin
from .models import Category

# Custom admin panel configuration for the Category model
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin configuration for managing categories.

    Features:
    - `prepopulated_fields`: Automatically generates the slug from `category_name`.
    - `list_display`: Shows category name and slug in the admin list view.
    """

    # Auto-generates slug based on the category name
    prepopulated_fields = {'slug': ('category_name',)}

    # Columns displayed in the admin list view
    list_display = ('category_name', 'slug')

# Registers the Category model with the custom admin configuration
admin.site.register(Category, CategoryAdmin)
