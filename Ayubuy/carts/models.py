from django.db import models  # Import Django's models module
from store.models import Product, Variation  # Import the Product, and Variation model from the store app

# Model for the shopping cart
class Cart(models.Model):
    """
    Represents a shopping cart session.

    Attributes:
    - `cart_id`: A unique identifier for the cart session (max 250 characters).
    - `date_added`: The date when the cart was created (auto-generated).
    """

    cart_id = models.CharField(max_length=250, blank=True)  # Unique session-based cart ID
    date_added = models.DateField(auto_now_add=True)  # Auto-set creation date

    def __str__(self):
        """
        Returns the cart ID as the string representation.
        """
        return self.cart_id


# Model for cart items
class CartItem(models.Model):
    """
    Represents a product added to the cart.

    Attributes:
    - `product`: ForeignKey linking to the `Product` model.
    - `cart`: ForeignKey linking to the `Cart` model.
    - `quantity`: Number of units of the product in the cart.
    - `is_active`: Boolean flag indicating if the cart item is still active (default: True).
    """

    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Product linked to the cart item
    variations = models.ManyToManyField(Variation, blank=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)  # Cart associated with the item
    quantity = models.IntegerField()  # Number of products in the cart
    is_active = models.BooleanField(default=True)  # Active status of the cart item
    
    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        """
        Returns the product name as the string representation.
        """
        return self.product.product_name  # Returns product name instead of the entire object
