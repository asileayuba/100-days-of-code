from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category

# Create your views here.

def store(request, category_slug=None):
    categories = None
    products = None
    
    if category_slug != None:
        categories = get_object_or_404(Category, category_slug=slug)
        products = product.objects.filter(category=categories, is_available=True)
        product_count = products.count()
    else:

        products = Product.objects.filter(is_available=True)  # Fetch available products
        product_count = products.count()  # Count the number of available products

    context = {
        'products': products,  # List of available products
        'product_count': product_count,  # Total number of available products
    }

    return render(request, 'store/store.html', context)  # Render store page with context
