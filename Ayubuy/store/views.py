from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.

def store(request, category_slug=None):
    categories = None
    products = None
    
    if category_slug != None:
        categories = get_object_or_404(Category, category_slug=Slug)
    """
    Renders the store page with a list of available products.

    Features:
    - Retrieves all products marked as available (`is_available=True`).
    - Counts the total number of available products.
    - Passes the product list and count as context data to the template.
    """

    products = Product.objects.filter(is_available=True)  # Fetch available products
    product_count = products.count()  # Count the number of available products

    context = {
        'products': products,  # List of available products
        'product_count': product_count,  # Total number of available products
    }

    return render(request, 'store/store.html', context)  # Render store page with context
