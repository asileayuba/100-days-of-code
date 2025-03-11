from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category

# Create your views here.

def store(request, category_slug=None):
    """
    Renders the store page with a list of available products.
    
    Features:
    - If a category is specified via `category_slug`, filters products by that category.
    - If no category is specified, retrieves all available products.
    - Counts the total number of available products.
    - Passes the product list and count as context data to the template.
    """

    categories = None  # Initialize category variable
    products = None  # Initialize product list

    if category_slug:
        # Retrieve the category object based on the provided slug, or return a 404 if not found
        categories = get_object_or_404(Category, slug=category_slug)
        
        # Filter products by the selected category and availability status
        products = Product.objects.filter(category=categories, is_available=True)
    else:
        # Retrieve all available products if no category is specified
        products = Product.objects.filter(is_available=True)

    product_count = products.count()  # Count the number of available products

    context = {
        'products': products,  # List of filtered/available products
        'product_count': product_count,  # Total number of available products
        'categories': categories,  # Pass the selected category (if any) for frontend use
    }

    return render(request, 'store/store.html', context)  # Render store page with context


def  product_detail(request, category_slug, product_slug):
    return render(request, 'store/product_detail.html')