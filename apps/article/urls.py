from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.article.views import ArticleListCreateAPIView, ArticleDetailAPIView, ArticleFileDetailAPIView, \
    ArticleFileListCreateAPIView

urlpatterns = [
    # 文章URL
    path('articles/', ArticleListCreateAPIView.as_view(), name='article-list-create'),
    path('articles/<int:pk>/', ArticleDetailAPIView.as_view(), name='article-detail'),

    # 文章文件URL
    path('article-files/', ArticleFileListCreateAPIView.as_view(), name='article-file-list-create'),
    path('article-files/<int:pk>/', ArticleFileDetailAPIView.as_view(), name='article-file-detail'),
    ]