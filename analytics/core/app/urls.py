from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("area_chart", views.area_chart, name="area_chart"),
    path("datatables", views.datatables, name="datatables"),
]
