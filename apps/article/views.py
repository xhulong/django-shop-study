from django.db.models import Prefetch
from django.http import Http404
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, mixins
from rest_framework.parsers import MultiPartParser, FormParser

from common.permissions import IsOwnerOrReadOnly
from .models import Article, ArticleFile
from .serializer import ArticleSerializer, ArticleFileSerializer, ArticleCreateSerializer
from ..global_system.models import AppConfiguration
from rest_framework.pagination import PageNumberPagination


class ArticlePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class ArticleListCreateAPIView(viewsets.GenericViewSet,mixins.ListModelMixin, mixins.CreateModelMixin):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly] # IsAuthenticated必须登录才能访问
    pagination_class = ArticlePagination
    serializer_class = ArticleSerializer

    def get_queryset(self):
        queryset = Article.objects.filter(is_delete=False, is_audit=1)
        return queryset
        # return Article.objects.filter(is_delete=False, is_audit=1)
    def list(self, request, *args, **kwargs):
        # 查询每个文章关联的用户信息，学校信息，文件信息
        # 比如用户头像，学校名称，文件路径
        queryset = self.get_queryset()
        print(queryset)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(data=serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        print()
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        app_config = AppConfiguration.objects.first()
        user = request.data.get('user')
        content = request.data.get('content')
        print(request.data)
        files = eval(request.data.get('files'))
        school = request.data.get('school')
        is_anonymous = request.data.get('is_anonymous')
        if eval(user) != request.user.id:
            return Response({'message': '不能为其他用户创建文章'}, status=status.HTTP_400_BAD_REQUEST)
        # 判断是否开启匿名
        if app_config.app_post_anonymous == False:
            is_anonymous = False
        # 帖子是否需要审核
        if app_config.app_post_audit == True:
            is_audit = 0
        else:
            is_audit = 1
        data = {
            'user': user,
            'content': content,
            'files': files,
            'school': school,
            'is_anonymous': is_anonymous,
            'is_audit': is_audit
        }
        serializer = ArticleCreateSerializer(data=data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data) # 获取头部信息
        return Response({'message': '发布成功'}, status=status.HTTP_200_OK, headers=headers)

# class ArticleListCreateAPIView(APIView):
#     permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
#     pagination_class = ArticlePagination
#     filter_backends = [SearchFilter]
#     search_fields = ['content']
#     def get(self, request, format=None):
#         articles = Article.objects.filter(is_delete=False, is_audit=1)
#         serializer = ArticleSerializer(articles, many=True, context={'request': request})
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         app_config = AppConfiguration.objects.first()
#         user = request.data.get('user')
#         content = request.data.get('content')
#         files = eval(request.data.get('files'))
#         school = request.data.get('school')
#         is_anonymous = request.data.get('is_anonymous')
#         if eval(user) != request.user.id:
#             return Response({'message': '不能为其他用户创建文章'}, status=status.HTTP_400_BAD_REQUEST)
#         # 判断是否开启匿名
#         if app_config.app_post_anonymous == False:
#             is_anonymous = False
#         # 帖子是否需要审核
#         if app_config.app_post_audit == True:
#             is_audit = 0
#         else:
#             is_audit = 1
#         data = {
#             'user': user,
#             'content': content,
#             'files': files,
#             'school': school,
#             'is_anonymous': is_anonymous,
#             'is_audit': is_audit
#         }
#         serializer = ArticleCreateSerializer(data=data, context={'request': request})
#         # print(serializer)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'message': '发布成功'}, status=status.HTTP_200_OK)
#         print(serializer.errors)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetailAPIView(APIView):
    """
    Retrieve, update or delete an article instance.
    """
    # permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]
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
        serializer = ArticleFileSerializer(data=request.data, context={'request': request})
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


