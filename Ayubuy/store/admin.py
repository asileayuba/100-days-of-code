from django.contrib import admin
from .models import Product, Variation, ReviewRating, ProductGallery
import admin_thumbnails


@admin_thumbnails.thumbnail('image')
class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1

# Admin configuration for the Product model
class ProductAdmin(admin.ModelAdmin):
    
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_date', 'is_available')  # Columns in admin list view
    list_filter = ('category', 'is_available', 'modified_date')  # Filters for easy data access
    search_fields = ('product_name', 'category__category_name')  # Enables search by product name & category
    prepopulated_fields = {'slug': ('product_name',)}  # Auto-populate slug from product name
    list_editable = ('price', 'stock', 'is_available')  # Allow quick inline edits
    inlines =[ProductGalleryInline]
    

class VariationAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Variation model.

    Features:
    - Displays product variations (category, value, active status).
    - Allows filtering and searching for better admin usability.
    """
    
    list_display = ('product', 'variation_category', 'variation_value', 'is_active')  # Display columns
    list_editable = ('is_active',)  # Enable inline editing of active status
    list_filter = ('product__category', 'product', 'variation_category', 'variation_value')  # Enhanced filtering
    search_fields = ('product__product_name', 'variation_category', 'variation_value')  # Search variations

# Register the models with custom admin settings
admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)
admin.site.register(ReviewRating)
admin.site.register(ProductGallery)
