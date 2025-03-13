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
]
