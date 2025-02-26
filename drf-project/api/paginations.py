from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomPagination(PageNumberPagination):
    # Allows clients to specify the number of items per page using 'page_size' query parameter
    page_size_query_param = 'page_size'

    # Custom query parameter for specifying the page number
    page_query_param = 'page-num'

    # Sets the maximum allowed page size to 1
    max_page_size = 1

    def get_paginated_response(self, data):
        """
        Customizes the paginated response to include additional details such as:
        - Next and previous page links
        - Total item count
        - Page size
        - The actual paginated results
        """
        return Response({
            'next': self.get_next_link(),  # Link to the next page if available
            'previous': self.get_previous_link(),  # Link to the previous page if available
            'count': self.page.paginator.count,  # Total number of items
            'page_size': self.page_size,  # Current page size
            'result': data  # Paginated data
        })
