from django.shortcuts import render
from store.models import Product

def home(request):
    """
    Renders the home page with a list of available products.

    - Fetches all products that are marked as available (`is_available=True`).
    - Passes the retrieved products as context data to the 'home.html' template.
    """

    products = Product.objects.filter(is_available=True)  # Fetch available products
    
    context = {
        'products': products,  # Context dictionary for template rendering
    }

    return render(request, 'home.html', context)  # Render home page with context
