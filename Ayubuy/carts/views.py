from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist  # Import ObjectDoesNotExist
from store.models import Product  # Import Product model
from .models import Cart, CartItem  # Import Cart and CartItem models


# Utility function to get or create a cart session ID
def _cart_id(request):
    """
    Retrieves the current session's cart ID.
    
    If a session key does not exist, a new session is created.
    This ensures each user (including anonymous users) has a unique cart.
    
    Args:
        request: The HTTP request object.

    Returns:
        str: The session key representing the cart ID.
    """
    cart = request.session.session_key  # Get current session key
    if not cart:
        cart = request.session.create()  # Create new session if none exists
    return cart


# View function to add a product to the cart
def add_cart(request, product_id):
    """
    Adds a product to the shopping cart.
    
    - If the cart does not exist, it creates one.
    - If the product is already in the cart, its quantity is increased.
    - If the product is not in the cart, a new cart item is created.

    Args:
        request: The HTTP request object.
        product_id (int): The ID of the product to be added.

    Returns:
        HttpResponseRedirect: Redirects to the cart page after adding the product.
    """
    product = Product.objects.get(id=product_id)  # Retrieve the product by ID

    # Retrieve or create a Cart object
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))  # Try to get the existing cart
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=_cart_id(request))  # Create a new cart if not found

    # Retrieve or create a CartItem for the product in the cart
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1  # Increase quantity if product already exists
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product=product,
            quantity=1,  # Default quantity is 1
            cart=cart,
        )

    return redirect('cart')  # Redirect to the cart page after adding the product

def remove_cart(request, product_id):
    cart =Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')


# View function to display the cart page
def cart(request, total=0, quantity=0, cart_items=None):
    """
    Displays the shopping cart page.

    Args:
        request: The HTTP request object.
        total (float): Total cost of items in the cart.
        quantity (int): Total quantity of items in the cart.
        cart_items (QuerySet): List of items in the cart.

    Returns:
        HttpResponse: Rendered cart page with cart details.
    """
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))  # Get the cart
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)  # Get active cart items
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)  # Calculate total cost
            quantity += cart_item.quantity  # Calculate total quantity
        tax = (2* total)/100
        grand_total = total + tax
    except ObjectDoesNotExist:
        cart_items = []  # If cart or cart items don't exist, set to empty list

    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax': tax,
        'grand_total': grand_total,
    }
    return render(request, 'store/cart.html', context)  # Render cart page


