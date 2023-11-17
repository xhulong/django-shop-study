# 自定义过滤
from django_filters import rest_framework as filters
from .models import Article

class ArticleFilter(filters.FilterSet):
    # user为外键，需要指定username
    user = filters.CharFilter(field_name='user__username')
    # school为外键，需要指定name
    school = filters.CharFilter(field_name='school__name')

    class Meta:
        model = Article
        fields = ['user', 'school', 'is_top', 'is_hot', 'is_anonymous', 'is_audit']
