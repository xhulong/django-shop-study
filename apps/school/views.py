from rest_framework import viewsets, mixins
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination

from .models import School
from .serializer import SchoolSerializer

class SchoolPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

# 只查询学校
class SchoolViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = School.objects.filter(is_delete=False, status=True)
    serializer_class = SchoolSerializer
    pagination_class = SchoolPagination
    filter_backends = [SearchFilter]
    search_fields = ['name', 'address']