from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist  # Import ObjectDoesNotExist for exception handling
from store.models import Product, Variation  # Import Product and Variation models from the store app
from .models import Cart, CartItem  # Import Cart and CartItem models
from django.http import HttpResponse


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
        cart = request.session.create()  # Create a new session if none exists
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
    product_variation = []
    if request.method == 'POST':
        for item in request.POST:
            key = item
            value = request.POST[key]
            
            try:
                variation = Variation.objects.get(
                    product=product, 
                    variation_category__iexact=key, 
                    variation_value__iexact=value
                )
                product_variation.append(variation)
            except:
                pass
        

    # Retrieve or create a Cart object
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))  # Try to get the existing cart
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=_cart_id(request))  # Create a new cart if not found

    # Retrieve or create a CartItem for the product in the cart
    is_cart_item_exists = CartItem.objects.filter(product=product, cart=cart).exists()
    if is_cart_item_exists:
        cart_item = CartItem.objects.filter(product=product, cart=cart)
        # existing_variations -> database
        # current variation -> product_variation
        # item_id -> database
        ex_var_list = []
        id = []
        for item in cart_item:
            existing_variation = item.variations.all()
            ex_var_list.append(list(existing_variation))
            id.append(item.id)
            
        print(ex_var_list)
        
        if product_variation in ex_var_list:
            # Increase the cart item quantity
            index = ex_var_list.index(product_variation)
            item_id = id[index]
            item = CartItem.objects.get(product=product, id=item_id)
            item.quantity += 1
            item.save()
        else:
            item = CartItem.objects.create(product=product, quantity=1, cart=cart)
            if len(product_variation) > 0:
                item.variations.clear()
                item.variations.add(*product_variation)
            item.save()
    else: 
        cart_item = CartItem.objects.create(
            product=product,
            quantity=1,  # Default quantity is 1
            cart=cart,
        )
        if len(product_variation) > 0:
            cart_item.variations.clear()
            cart_item.variations.add(*product_variation)
        cart_item.save()
    return redirect('cart')  # Redirect to the cart page after adding the product


# View function to remove a single unit of a product from the cart
def remove_cart(request, product_id, cart_item_id):
    """
    Removes one quantity of a product from the cart.
    
    - If more than one quantity exists, it decreases the quantity.
    - If only one quantity exists, it removes the cart item completely.

    Args:
        request: The HTTP request object.
        product_id (int): The ID of the product to be removed.

    Returns:
        HttpResponseRedirect: Redirects to the cart page after modification.
    """
    cart = Cart.objects.get(cart_id=_cart_id(request))  # Get the cart object
    product = get_object_or_404(Product, id=product_id)  # Get the product or return 404 if not found
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart, id=cart_item_id)  # Get the cart item

        if cart_item.quantity > 1:
            cart_item.quantity -= 1  # Decrease quantity if more than one exists
            cart_item.save()
        else:
            cart_item.delete()  # Remove the cart item if only one exists     
    except CartItem.DoesNotExist:
        pass  # Prevents errors if the cart item is not found

    return redirect('cart')  # Redirect to the cart page


# View function to completely remove a product from the cart
def remove_cart_item(request, product_id, cart_item_id):
    """
    Completely removes a product from the shopping cart.
    
    Args:
        request: The HTTP request object.
        product_id (int): The ID of the product to be removed.

    Returns:
        HttpResponseRedirect: Redirects to the cart page after deletion.
    """
    cart = Cart.objects.get(cart_id=_cart_id(request))  # Get the cart object
    product = get_object_or_404(Product, id=product_id)  # Get the product or return 404 if not found
    cart_item = CartItem.objects.get(product=product, cart=cart, id=cart_item_id)  # Get the cart item
    cart_item.delete()  # Remove the cart item completely

    return redirect('cart')  # Redirect to the cart page


# View function to display the cart page
def cart(request, total=0, quantity=0, cart_items=None):
    """
    Displays the shopping cart page.
    
    - Retrieves cart details such as total price and quantity.
    - If the cart is empty, displays an empty cart message.

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
        
        # Calculate total price and quantity
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)  # Total cost
            quantity += cart_item.quantity  # Total quantity of items
        
        tax = (2 * total) / 100  # 2% tax on total
        grand_total = total + tax  # Calculate grand total including tax

    except ObjectDoesNotExist:
        cart_items = []  # If the cart does not exist, set cart items to an empty list
        tax = 0
        grand_total = 0

    # Prepare context data for rendering
    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax': tax,
        'grand_total': grand_total,
    }

    return render(request, 'store/cart.html', context)  # Render the cart page


def checkout(request, total=0, quantity=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))  # Get the cart
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)  # Get active cart items
        
        # Calculate total price and quantity
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)  # Total cost
            quantity += cart_item.quantity  # Total quantity of items
        
        tax = (2 * total) / 100  # 2% tax on total
        grand_total = total + tax  # Calculate grand total including tax

    except ObjectDoesNotExist:
        cart_items = []  # If the cart does not exist, set cart items to an empty list
        tax = 0
        grand_total = 0

    # Prepare context data for rendering
    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax': tax,
        'grand_total': grand_total,
    }
    return render(request, 'store/checkout.html', context)