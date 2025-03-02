from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomPagination(PageNumberPagination):

    # Enables dynamic page size via query param
    page_size_query_param = 'page_size'

    # Uses 'page-num' instead of default 'page'
    page_query_param = 'page-num'

    # Allows up to 100 items per page
    max_page_size = 10

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
