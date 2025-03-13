from django.urls import path  # Import the path function for URL routing
from . import views  # Import views from the current app

# Define URL patterns for the cart functionality
urlpatterns = [
    path('', views.cart, name='cart'),  
    # Route for displaying the cart page

    path('add_cart/<int:product_id>/', views.add_cart, name='add_cart'),
    # Route for adding a product to the cart
    # `<int:product_id>` ensures that only integer values are passed as product IDs

    path('remove_cart/<int:product_id>/', views.remove_cart, name='remove_cart'),
    # Route for reducing the quantity of a product in the cart by 1
    # If the quantity is greater than 1, it decreases; otherwise, the item is removed

    path('remove_cart_item/<int:product_id>/', views.remove_cart_item, name='remove_cart_item'),
    # Route for completely removing a specific product from the cart
]
