from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product
from .models import Cart, CartItem

# Generate a unique cart ID for the session
def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        request.session.create()  # Create session only if it doesn't exist
        cart = request.session.session_key
    return cart

# Add product to cart
def add_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)  # Ensure product exists

    # Get or create a cart using session ID
    cart, created = Cart.objects.get_or_create(cart_id=_cart_id(request))

    # Check if the product is already in the cart
    cart_item, created = CartItem.objects.get_or_create(product=product, cart=cart)
    
    # If the item already exists, increment quantity
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    return redirect('cart')

# Display cart items
def cart(request):
    cart = None
    cart_items = []
    
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))  # Get cart by session
        cart_items = CartItem.objects.filter(cart=cart)  # Retrieve cart items
    except Cart.DoesNotExist:
        pass  # If the cart doesn't exist, cart_items remains an empty list

    context = {
        'cart_items': cart_items,
    }

    return render(request, 'store/cart.html', context)
