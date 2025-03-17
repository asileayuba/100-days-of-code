from django.contrib import admin
from .models import Cart, CartItem

# Register your models with custom admin configurations.

class CartAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'date_added')  # Display cart ID and date added in the admin panel

class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'cart', 'quantity', 'is_active')  # Show product, cart, quantity, and status

# Register the models with their respective admin classes
admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
