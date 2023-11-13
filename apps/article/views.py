from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from common.permissions import IsOwnerOrReadOnly
from .models import Article, ArticleComment, ArticleLike, ArticleView, ArticleFile
from .serializer import ArticleSerializer, ArticleCommentSerializer, ArticleLikeSerializer, ArticleViewSerializer, ArticleFileSerializer


class Article(APIView):
    def get(self, request):


    def post(self, request):
        pass
