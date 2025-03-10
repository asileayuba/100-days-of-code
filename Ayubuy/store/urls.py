from django.urls import path
from . import views

# Define URL patterns for the store app
urlpatterns = [
    path('', views.store, name='store'),  # Route for viewing all available products
    path('<slug:category_slug>/', views.store, name='products_by_category'),  # Route for filtering by category
]
