from django.urls import path
from . import views


urlpatterns = [
    # Students Paths
    path('students/', views.studentsViews),
    path('students/<int:pk>/', views.studentDetailView),
    
    # Employees Path
    path('employees/', views.Employees.as_view())
]
