from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('employees', views.EmployeeViewset, basename='employee')

urlpatterns = [
    # Students Paths
    path('students/', views.studentsViews),
    path('students/<int:pk>/', views.studentDetailView),
    
    # Employees Path
    # path('employees/', views.Employees.as_view()),
    # path('employees/<int:pk>', views.EmployeeDetail.as_view()),
    
    path('', include(router.urls))
]
