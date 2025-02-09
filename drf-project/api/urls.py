from django.urls import path
from . import views


urlpatterns = [
    path('students/', views.studentsViews),
    path('student/<int:pk>/', views.studentDetailView),
]
