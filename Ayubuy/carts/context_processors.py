from .models import Cart, CartItem  # Import Cart and CartItem models from the current app
from .views import _cart_id  # Import the utility function to retrieve the cart ID


def counter(request):
    """
    Calculates the total quantity of items in the user's cart.

    This function runs as a context processor, making `cart_count` available in all templates.
    It ensures that only non-admin pages count the cart items.

    Args:
        request: The HTTP request object.

    Returns:
        dict: A dictionary containing the total quantity of items in the cart (`cart_count`).
    """
    cart_count = 0  # Initialize cart item count

    # Prevent counting the cart items in the admin panel
    if 'admin' in request.path:
        return {}

    try:
        # Retrieve the cart associated with the current session ID
        cart = Cart.objects.filter(cart_id=_cart_id(request))

        # Retrieve all items belonging to the first cart in the queryset
        cart_items = CartItem.objects.all().filter(cart=cart[:1])

        # Sum up the quantity of all cart items
        for cart_item in cart_items:
            cart_count += cart_item.quantity

    except Cart.DoesNotExist:
        cart_count = 0  # If no cart exists, set cart_count to 0

    return dict(cart_count=cart_count)  # Return cart count as a dictionary for template usage
