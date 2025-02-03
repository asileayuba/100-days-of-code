from django.urls import path
from . import views

urlpatterns = [
    path('total_views', views.total_views, name='api_total_views'), 
    path('datatable_api/', views.datatable_api, name='datatable_api'),
    path('movies/', views.movies, name='movies_api'),
    path('movies_with_ratings/', views.movies_with_ratings, name='movies_with_ratings_api'),
]
