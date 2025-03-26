from django.shortcuts import render
from django.http import HttpResponse
from carts.models import CartItem



def place_order(request):
    current_user = request.user
    
    
    # If the cart count is less than or equal to zero, then redirect back to shop
    cart_items = CartItem.objects.filter(user=current_user)
    cart_count = cart_items.count()
    if cart_count <= 0:
        return redirect('store')
