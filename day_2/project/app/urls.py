from django.urls import path
from app import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("services", views.services, name="services"),
    path("contact", views.contact, name="contact"),
    path("blog", views.handleBlog, name="handleBlog"),
    path("search", views.search, name="search"),
    path("login", views.handlelogin, name="handlelogin"),
    path("logout", views.handlelogout, name="handlelogout"),
    path("signup", views.handlesignup, name="handlesignup"),
]
