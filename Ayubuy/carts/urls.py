from django.urls import path  # Import path for defining URL routes
from . import views  # Import views from the current app

# URL patterns for cart functionality
urlpatterns = [
    path('', views.cart, name='cart'),  
    # Display the cart page

    path('add_cart/<int:product_id>/', views.add_cart, name='add_cart'),
    # Add a product to the cart using its product ID

    path('remove_cart/<int:product_id>/<int:cart_item_id>/', views.remove_cart, name='remove_cart'),
    # Decrease the quantity of a cart item; remove it if quantity becomes zero

    path('remove_cart_item/<int:product_id>/<int:cart_item_id>/', views.remove_cart_item, name='remove_cart_item'),
    # Remove a cart item completely from the cart
    
    path('checkout/', views.checkout, name="checkout"),
]
