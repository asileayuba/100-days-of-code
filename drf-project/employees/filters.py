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
    
    designation = django_filters.CharFilter(
        field_name='designation', 
        lookup_expr='iexact'
    )  # Case-insensitive filter for designation

    emp_name = django_filters.CharFilter(
        field_name='emp_name', 
        lookup_expr='icontains'
    )  # Allows partial matching for employee names

    # id = django_filters.RangeFilter(field_name='id')  # Filter employees within an ID range

    id_min = django_filters.CharFilter(
        method='filter_by_id_range', 
        label='From EMP ID'
    )  # Filters employees with ID greater than or equal to the given value

    id_max = django_filters.CharFilter(
        method='filter_by_id_range', 
        label='To EMP ID'
    )  # Filters employees with ID less than or equal to the given value

    class Meta:
        model = Employee  # Specifies the model being filtered
        fields = ['designation', 'emp_name', 'id_min', 'id_max']  # Defines available filter fields
        
    def filter_by_id_range(self, queryset, name, value):
        """
        Custom filtering method to apply range filters on employee IDs.

        - `id_min`: Filters employees with ID greater than or equal to the given value.
        - `id_max`: Filters employees with ID less than or equal to the given value.

        Args:
            queryset: The initial queryset of Employee objects.
            name: The name of the filter field.
            value: The filter value provided by the user.

        Returns:
            Filtered queryset based on the specified ID range.
        """
        if name == 'id_min':
            return queryset.filter(emp_id__gte=value)
        elif name == 'id_max':
            return queryset.filter(emp_id__lte=value)
        return queryset
