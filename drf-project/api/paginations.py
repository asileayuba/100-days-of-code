from rest_framework.pagination import PageNumberPagination
from rest_framework.response import ResponseNotReady

class CustomPagination(PageNumberPagination):
    page_size_query_param = 'page_size'
    page_query_param = 'page-num'
    max_page_size =1
    