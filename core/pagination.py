from rest_framework import pagination
from rest_framework.response import Response


class LargeResultsSetPagination(pagination.PageNumberPagination):
    page_size = 200
    page_size_query_param = "page_size"
    max_page_size = 10000

    def get_paginated_response(self, data):
        return Response(data)


class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 50
    page_size_query_param = "page_size"
    max_page_size = 1000

    def get_paginated_response(self, data):
        return Response(data)
