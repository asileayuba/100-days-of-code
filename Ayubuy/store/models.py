from django.db import models
from category.models import Category
from django.urls import reverse
from decimal import Decimal
from accounts.models import Account
from django.db.models import Avg,Count

# Model definition for products
class Product(models.Model):
    """
    Represents a product in the system.
    """

    product_name = models.CharField(max_length=200, unique=True)  # Product name (unique)
    slug = models.SlugField(max_length=200, unique=True)  # SEO-friendly unique slug
    description = models.TextField(max_length=500, blank=True)  # Optional product description
    price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))  # Precise price handling
    images = models.ImageField(upload_to='photos/products')  # Product image storage path
    stock = models.PositiveIntegerField()  # Prevents negative stock values
    is_available = models.BooleanField(default=True)  # Product availability status
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Category association
    created_date = models.DateTimeField(auto_now_add=True)  # Auto-set creation timestamp
    modified_date = models.DateTimeField(auto_now=True)  # Auto-update modification timestamp

    def get_url(self):
        """
        Returns the absolute URL for the product detail page.
        """
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name
    
    def averageReview(self):
        reviews = ReviewRating.objects.filter(product=self, status=True).aggregate(average=Avg('rating'))
        avg = 0
        if reviews['average'] is not None:
            avg = float(reviews['average'])
        return avg
    
    def countReview(self):
        reviews = ReviewRating.objects.filter(product=self, status=True).aggregate(count=Count('id'))
        count = 0
        if reviews['count'] is not None:
            count = int(reviews['count'])
        return count

    class Meta:
        ordering = ['-created_date']
        verbose_name = "Product"
        verbose_name_plural = "Products"
        
        
class VariationManager(models.Manager):
    def colors(self):
        return super(VariationManager, self).filter(variation_category='color', is_active=True)
    
    def sizes(self):
        return super(VariationManager, self).filter(variation_category='size', is_active=True)


# Variation choices should be a tuple of tuples instead of a set
VARIATION_CATEGORY_CHOICES = (
    ('color', 'Color'),
    ('size', 'Size'),
)

class Variation(models.Model):
    """
    Represents a product variation such as color or size.
    """

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="variations")
    variation_category = models.CharField(max_length=100, choices=VARIATION_CATEGORY_CHOICES)
    variation_value = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now=True)
    
    objects = VariationManager()

    def __str__(self):
        return f"{self.variation_category}: {self.variation_value}"

    class Meta:
        ordering = ['product', 'variation_category']
        verbose_name = "Variation"
        verbose_name_plural = "Variations"
        
        
class ReviewRating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100, blank=True)
    review = models.TextField(max_length=500, blank=True)
    rating = models.FloatField()
    ip = models.CharField(max_length=20, blank=True)
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.subject


class ProductGallery(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='store/products/', max_length=255)
    
    def __str__(self):
        return self.product.product_name
    
    class Meta:
        verbose_name = 'productgallery'
        verbose_name_plural = 'product gallery'