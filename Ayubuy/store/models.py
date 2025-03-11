from django.db import models
from category.models import Category
from django.urls import reverse

# Model definition for products
class Product(models.Model):
    """
    Represents a product in the system.

    Attributes:
    - `product_name`: Unique name of the product (max 200 characters).
    - `slug`: Unique slug for SEO-friendly URLs (max 200 characters).
    - `description`: Optional detailed description (max 500 characters).
    - `price`: Product price stored as a float.
    - `images`: Product image, stored in `photos/products`.
    - `stock`: Number of available units.
    - `is_available`: Boolean flag indicating availability status (default: True).
    - `category`: ForeignKey linking to the `Category` model.
    - `created_date`: Timestamp when the product is created (auto-generated).
    - `modified_date`: Timestamp when the product is last modified (auto-updated).

    Methods:
    - `__str__()`: Returns the product name as a string representation.
    """

    product_name = models.CharField(max_length=200, unique=True)  # Product name (unique)
    slug = models.SlugField(max_length=200, unique=True)  # SEO-friendly unique slug
    description = models.TextField(max_length=500, blank=True)  # Optional product description
    price = models.FloatField()  # Product price
    images = models.ImageField(upload_to='photos/products')  # Product image storage path
    stock = models.IntegerField()  # Available stock quantity
    is_available = models.BooleanField(default=True)  # Product availability status
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Category association
    created_date = models.DateTimeField(auto_now_add=True)  # Auto-set creation timestamp
    modified_date = models.DateTimeField(auto_now_add=True)  # Auto-set modification timestamp
    
    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        """
        Returns a string representation of the product.
        """
        return self.product_name
