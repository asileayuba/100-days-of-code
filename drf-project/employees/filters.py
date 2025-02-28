import django_filters
from .models import Employee




class EmployeeFilter(django_filters.FilterSet):
    designation = django_filters.CharFilter(field_name='designation', look_expr='iexact')
    
