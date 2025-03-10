from django.db import models
from django.urls import reverse

# Model definition for product categories
class Category(models.Model):
    """
    Represents a product category in the system.

    Attributes:
    - `category_name`: Name of the category (max 50 characters).
    - `slug`: Unique slug for URL handling (max 100 characters).
    - `description`: Optional category description (max 225 characters).
    - `cat_image`: Optional image field for category images, stored in `photos/categories`.

    Metadata:
    - `verbose_name`: Singular form for admin display.
    - `verbose_name_plural`: Plural form for admin display.
    """

    category_name = models.CharField(max_length=50)  # Category name with a max length of 50
    slug = models.SlugField(max_length=100, unique=True)  # Unique slug for category URLs
    description = models.TextField(max_length=225, blank=True)  # Optional category description
    cat_image = models.ImageField(upload_to='photos/categories', blank=True)  # Optional category image

    class Meta:
        verbose_name = 'category'  # Singular name in admin panel
        verbose_name_plural = 'categories'  # Plural name in admin panel
        
    def get_url(self):
        return reverse('products_by_category', args=[self.slug])

    def __str__(self):
        """
        Returns a string representation of the category.
        """
        return self.category_name
