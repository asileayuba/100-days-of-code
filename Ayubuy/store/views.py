from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category
from carts.models import CartItem
from django.db.models import Q
from carts.views import _cart_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse

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
        paginator = Paginator(products, 1)  # Consider making this configurable
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
    else:
        # Fetch all available products if no category filter is applied
        products = Product.objects.filter(is_available=True).order_by('id')  # Explicit ordering field may help
        paginator = Paginator(products, 3)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()  # Count the number of available products

    context = {
        'products': paged_products,  # List of filtered/available products
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
        # Consider logging this exception for debugging purposes
    
    context = {
        'single_product': single_product,  # Pass the retrieved product to the template
        'in_cart': in_cart,  # Boolean indicating if the product is already in the cart
    }

    return render(request, 'store/product_detail.html', context)  # Render product details page


def search(request):
    """
    Handles product search functionality.

    Features:
    - Retrieves the search keyword from the request.
    - Filters products based on the keyword match in the product name or description.
    - Orders results by creation date in descending order.
    - Counts the total number of matching products.
    - Passes the search results and count as context data to the template.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - HTTP response rendering the 'store/store.html' template with search results.
    """

    products = []  # Initialize product list to prevent errors if no keyword is provided
    product_count = 0  # Initialize product count

    if 'keyword' in request.GET:  # Check if a search query exists in request
        keyword = request.GET['keyword']
        if keyword:
            # Filter products that match the search keyword in name or description
            products = Product.objects.order_by('-created_date').filter(
                Q(description__icontains=keyword) | Q(product_name__icontains=keyword)
            )
            product_count = products.count()  # Count the number of matching products

    context = {
        'products': products,  # Pass the list of found products
        'product_count': product_count,  # Total number of matched products
    }

    return render(request, 'store/store.html', context)  # Render the store page with search results
