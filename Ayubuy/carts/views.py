from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist  # Import ObjectDoesNotExist for exception handling
from store.models import Product, Variation  # Import Product and Variation models from the store app
from .models import Cart, CartItem  # Import Cart and CartItem models
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Utility function to get or create a cart session ID
def _cart_id(request):
    if not request.session.session_key:
        request.session.create()
    return request.session.session_key


# View function to add a product to the cart
def add_cart(request, product_id):
    current_user = request.user
    product = Product.objects.get(id=product_id)
    
    # If the user is authenticated
    if current_user.is_authenticated:
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
            
        # Retrieve or create a CartItem for the product in the cart
        is_cart_item_exists = CartItem.objects.filter(product=product, user=current_user).exists()
        if is_cart_item_exists:
            cart_item = CartItem.objects.filter(product=product, user=current_user)
            ex_var_list = []
            id = []
            for item in cart_item:
                existing_variation = item.variations.all()
                ex_var_list.append(list(existing_variation))
                id.append(item.id)
            
            if product_variation in ex_var_list:
                # Increase the cart item quantity
                index = ex_var_list.index(product_variation)
                item_id = id[index]
                item = CartItem.objects.get(product=product, id=item_id)
                item.quantity += 1
                item.save()
            else:
                item = CartItem.objects.create(product=product, quantity=1, user=current_user)
                if len(product_variation) > 0:
                    item.variations.clear()
                    item.variations.add(*product_variation)
                item.save()
        else: 
            cart_item = CartItem.objects.create(
                product=product,
                quantity=1,  # Default quantity is 1
                user=current_user,
            )
            if len(product_variation) > 0:
                cart_item.variations.clear()
                cart_item.variations.add(*product_variation)
            cart_item.save()
        return redirect('cart')
    
    # If the user is not authenticated
    else:
        
     # Retrieve the product by ID
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
   
    product = get_object_or_404(Product, id=product_id) 
    try:
        if request.user.is_authenticated:
            cart_item = CartItem.objects.get(product=product, user=request.user, id=cart_item_id)
        else:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_item = CartItem.objects.get(product=product, cart=cart, id=cart_item_id) 

        if cart_item.quantity > 1:
            cart_item.quantity -= 1 
            cart_item.save()
        else:
            cart_item.delete() 
    except CartItem.DoesNotExist:
        pass 

    return redirect('cart')  


# View function to completely remove a product from the cart
def remove_cart_item(request, product_id, cart_item_id):
    
    product = get_object_or_404(Product, id=product_id)
    if request.user.is_authenticated:
        cart_item = CartItem.objects.get(product=product, user=request.user, id=cart_item_id)
    else:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_item = CartItem.objects.get(product=product, cart=cart, id=cart_item_id)
    cart_item.delete()
    return redirect('cart') 


# View function to display the cart page
def cart(request, total=0, quantity=0, cart_items=None):
   
    try:
        if request.user.is_authenticated:
            cart_items = CartItem.objects.filter(user=request.user, is_active=True)
        else: 
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

@login_required(login_url='login')
def checkout(request, total=0, quantity=0, cart_items=None):
    try:
        if request.user.is_authenticated:
            cart_items = CartItem.objects.filter(user=request.user, is_active=True)
        else: 
            cart = Cart.objects.get(cart_id=_cart_id(request)) 
            cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        
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