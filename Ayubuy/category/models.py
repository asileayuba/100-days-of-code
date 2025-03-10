from django.db import models
from django.urls import reverse

# Model definition for product categories
class Category(models.Model):
    """
    Represents a product category in the system.

    Attributes:
    - `category_name` (str): Name of the category (max 50 characters).
    - `slug` (str): Unique slug for URL handling (max 100 characters).
    - `description` (str, optional): Brief category description (max 225 characters).
    - `cat_image` (ImageField, optional): Category image stored in `photos/categories`.

    Methods:
    - `get_url()`: Returns the URL for accessing products within this category.

    Metadata:
    - `verbose_name`: Singular form for admin display.
    - `verbose_name_plural`: Plural form for admin display.
    """

    category_name = models.CharField(max_length=50, unique=True)  # Ensures category names are unique
    slug = models.SlugField(max_length=100, unique=True)  # Unique identifier for category URLs
    description = models.TextField(max_length=225, blank=True)  # Optional description
    cat_image = models.ImageField(upload_to='photos/categories', blank=True)  # Optional image field

    class Meta:
        verbose_name = 'category'  # Singular name in admin panel
        verbose_name_plural = 'categories'  # Plural name in admin panel

    def get_url(self):
        """
        Generates the category-specific URL for filtering products.
        """
        return reverse('products_by_category', args=[self.slug])

    def __str__(self):
        """
        Returns the category name as its string representation.
        """
        return self.category_name
