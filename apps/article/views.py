from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Article, ArticleFile
from .serializer import ArticleSerializer, ArticleFileSerializer

class ArticleListCreateAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    """
    List all articles or create a new article.
    """
    def get(self, request, format=None):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ArticleSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            # 添加文件
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArticleDetailAPIView(APIView):
    """
    Retrieve, update or delete an article instance.
    """
    def get_object(self, pk):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ArticleFileListCreateAPIView(APIView):
    """
    List all article files or create a new article file.
    """
    parser_classes = (MultiPartParser, FormParser,)

    def get(self, request, format=None):
        article_files = ArticleFile.objects.all()
        serializer = ArticleFileSerializer(article_files, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ArticleFileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArticleFileDetailAPIView(APIView):
    """
    Retrieve, update or delete an article file instance.
    """
    def get_object(self, pk):
        try:
            return ArticleFile.objects.get(pk=pk)
        except ArticleFile.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        article_file = self.get_object(pk)
        serializer = ArticleFileSerializer(article_file)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        article_file = self.get_object(pk)
        serializer = ArticleFileSerializer(article_file, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        article_file = self.get_object(pk)
        article_file.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


