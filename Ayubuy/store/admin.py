from django.contrib import admin
from .models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Product model.

    Features:
    - Displays key product details (name, price, stock, category, modified date, and availability).
    - Auto-generates slug field from product name for SEO-friendly URLs.
    """
    
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_date', 'is_available')  # Columns in admin list view
    prepopulated_fields = {'slug': ('product_name',)}  # Auto-populate slug from product name

# Register the Product model with custom admin settings
admin.site.register(Product, ProductAdmin)
