# 自定义过滤
from django_filters import rest_framework as filters
from .models import Article

class ArticleFilter(filters.FilterSet):
    user = filters.NumberFilter(field_name='user', lookup_expr='exact')
    class Meta:
        model = Article
        fields = ['content', 'user', 'school', 'is_audit']
