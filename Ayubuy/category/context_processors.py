from .models import Category

def menu_links(request):
    """
    Context processor to make product categories globally available in templates.

    Returns:
    - A dictionary containing all categories, accessible via 'links' in templates.
    """
    links = Category.objects.all()  # Retrieve all category objects
    return {'links': links}  # Return as a dictionary for template context
