import django_filters
from .models import Employee

class EmployeeFilter(django_filters.FilterSet):
    """
    A filter class for the Employee model.
    
    - Allows filtering employees based on the 'designation' field.
    - Uses case-insensitive exact matching (iexact) for better flexibility.
    """
    
    designation = django_filters.CharFilter(field_name='designation', lookup_expr='iexact')  # Case-insensitive filter
    emp_name = django_filters.CharFilter(field_name='emp_name', lockup_expr='icontains')

    class Meta:
        model = Employee  # Specifies the model being filtered
        fields = ['designation']  # Defines the fields available for filtering
