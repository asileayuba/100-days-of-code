import django_filters
from .models import Employee

class EmployeeFilter(django_filters.FilterSet):
    """
    A filter class for the Employee model.

    Features:
    - Designation Filter: Case-insensitive exact match (`iexact`).
    - Employee Name Search: Allows partial matches (`icontains`).
    - ID Range Filter: Enables filtering employees within a specific ID range.

    These filters enhance search functionality and improve data retrieval flexibility.
    """
    
    designation = django_filters.CharFilter(field_name='designation', lookup_expr='iexact')  # Case-insensitive filter
    emp_name = django_filters.CharFilter(field_name='emp_name', lookup_expr='icontains')  # Partial match for name search
    # id = django_filters.RangeFilter(field_name='id')  # Filter employees within an ID range
    id_min = django_filters.CharFilter(method='filter_by_id_range')
    id_max = django_filters.CharFilter(method='filter_by_id_range')

    class Meta:
        model = Employee  # Specifies the model being filtered
        fields = ['designation', 'emp_name']  # Defines the fields available for filtering
        
        
    def filter_by_id_range(self, queryset, name, value):
