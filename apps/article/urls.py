from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.article.views import ArticleListCreateGenericViewSet, ArticleDetailAPIView, ArticleFileDetailAPIView, \
    ArticleFileListCreateAPIView, ArticleLikeGenericViewSet, ArticleViewGenericViewSet, ArticleCommentGenericViewSet

urlpatterns = [
    # 文章URL
    path('articles/', ArticleListCreateGenericViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('articles/<int:pk>/', ArticleDetailAPIView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    # 文章文件URL
    path('article-files/', ArticleFileListCreateAPIView.as_view()),
    path('article-files/<int:pk>/', ArticleFileDetailAPIView.as_view()),
    # 点赞
    path('article-likes/<int:pk>/', ArticleLikeGenericViewSet.as_view({'post': 'create', 'delete': 'destroy'})),
    # 浏览
    path('article-views/<int:pk>/', ArticleViewGenericViewSet.as_view({'put': 'update'})),
    # 文章评论 retrieve:获取该评论回复评论, list:获取文章的所有评论, create:创建评论
    path('article-comments/<int:pk>/', ArticleCommentGenericViewSet.as_view({'get': 'list', 'post': 'create'})),
    ]