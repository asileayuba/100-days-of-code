from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category
from carts.models import CartItem
from carts.views import _cart_id

# Create your views here.

def store(request, category_slug=None):
    """
    Renders the store page with a list of available products.

    Features:
    - If a category is specified via `category_slug`, filters products by that category.
    - If no category is specified, retrieves all available products.
    - Counts the total number of available products.
    - Passes the product list and count as context data to the template.

    Parameters:
    - request: The HTTP request object.
    - category_slug (str, optional): The slug of the category to filter products.

    Returns:
    - HTTP response rendering the 'store/store.html' template with product data.
    """

    categories = None  # Initialize category variable to store the selected category
    products = None  # Initialize product list

    if category_slug:
        # Retrieve the category object based on the provided slug, or return a 404 if not found
        categories = get_object_or_404(Category, slug=category_slug)
        
        # Fetch products belonging to the selected category and that are available
        products = Product.objects.filter(category=categories, is_available=True)
    else:
        # Fetch all available products if no category filter is applied
        products = Product.objects.filter(is_available=True)

    product_count = products.count()  # Count the number of available products

    context = {
        'products': products,  # List of filtered/available products
        'product_count': product_count,  # Total number of available products
        'categories': categories,  # Pass the selected category (if any) for frontend use
    }

    return render(request, 'store/store.html', context)  # Render the store page with context data


def product_detail(request, category_slug, product_slug):
    """
    Displays the details of a specific product.

    Features:
    - Retrieves a single product based on both its category and product slug.
    - Checks if the product is already in the cart for the current session.
    - Handles exceptions in case the product does not exist.
    - Passes the product details as context data to the template.

    Parameters:
    - request: The HTTP request object.
    - category_slug (str): The slug of the category the product belongs to.
    - product_slug (str): The unique slug of the product.

    Returns:
    - HTTP response rendering the 'store/product_detail.html' template with product details.
    """

    try:
        # Fetch the product based on category slug and product slug
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)

        # Check if the product exists in the cart for the current session
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()

    except Product.DoesNotExist:
        single_product = None  # Handle the case where the product is not found
        in_cart = False  # Ensure in_cart is False if the product does not exist
    
    context = {
        'single_product': single_product,  # Pass the retrieved product to the template
        'in_cart': in_cart,  # Boolean indicating if the product is already in the cart
    }

    return render(request, 'store/product_detail.html', context)  # Render product details page
