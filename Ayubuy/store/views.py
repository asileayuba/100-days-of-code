from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, ReviewRating
from category.models import Category
from carts.models import CartItem
from django.db.models import Q
from carts.views import _cart_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
from .forms import ReviewForm
from django.contrib import messages
from orders.models import OrderProduct

# Create your views here.

def store(request, category_slug=None):
    

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

    try:
        # Fetch the product based on category slug and product slug
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)

        # Check if the product exists in the cart for the current session
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()

    except Product.DoesNotExist:
        single_product = None  # Handle the case where the product is not found
        in_cart = False  # Ensure in_cart is False if the product does not exist
       
    # Ensure the  user is authenticated before checking order history
    orderproduct = False    # Default value
    if request.user.is_authenticated:
        orderproduct = OrderProduct.objects.filter(user=request.user, product_id=single_product.id).exists()
        
    # Get the reviews
    reviews = ReviewRating.objects.filter(product_id=single_product.id, status=True)
    
    context = {
        'single_product': single_product,  # Pass the retrieved product to the template
        'in_cart': in_cart,  # Boolean indicating if the product is already in the cart
        'orderproduct': orderproduct,
        'reviews': reviews,
    }

    return render(request, 'store/product_detail.html', context)  # Render product details page


def search(request):

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


def submit_review(request, product_id):
    url = request.META.get('HTTP_REFERER')
    
    if request.method == "POST":

        try:
            reviews = ReviewRating.objects.get(user__id=request.user.id, product__id=product_id)
            form = ReviewForm(request.POST, instance=reviews)
            if form.is_valid():
                form.save()
                messages.success(request, "Thank you! Your review has been updated.")
            return redirect(url)

        except ReviewRating.DoesNotExist:
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = ReviewRating()
                data.subject = form.cleaned_data['subject']
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                data.ip = request.META.get('REMOTE_ADDR')
                data.product_id = product_id
                data.user_id = request.user.id
                data.save()
                messages.success(request, "Thank you! Your review has been submitted.")
            return redirect(url)
