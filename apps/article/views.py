from django.http import Http404
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, mixins
from rest_framework.parsers import MultiPartParser, FormParser

from common.permissions import IsOwnerOrReadOnly
from .filters import ArticleFilter
from .models import Article, ArticleFile, ArticleLike, ArticleView, ArticleComment
from .serializer import ArticleSerializer, ArticleFileSerializer, ArticleCreateSerializer, ArticleLikeSerializer, \
    ArticleViewSerializer, ArticleCommentSerializer, ArticleCommentCreateSerializer
from ..global_system.models import AppConfiguration
from rest_framework.pagination import PageNumberPagination


class ArticlePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class ArticleListCreateGenericViewSet(viewsets.GenericViewSet,mixins.ListModelMixin, mixins.CreateModelMixin):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly] # IsAuthenticated必须登录才能访问
    pagination_class = ArticlePagination
    serializer_class = ArticleSerializer
    filterset_class = ArticleFilter

    def get_queryset(self):
        queryset = Article.objects.filter(is_delete=False, is_audit=1).order_by('-is_top', '-is_hot', '-create_time')
        return queryset
    # def list(self, request, *args, **kwargs):
    #     # 查询每个文章关联的用户信息，学校信息，文件信息
    #     # 比如用户头像，学校名称，文件路径
    #     queryset = self.get_queryset()
    #     page = self.paginate_queryset(queryset)
    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True, context={'request': request})
    #         return self.get_paginated_response(data=serializer.data)
    #     serializer = self.get_serializer(queryset, many=True, context={'request': request})
    #     print()
    #     return Response(serializer.data)

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


class ArticleDetailAPIView(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = ArticleSerializer
    queryset = Article.objects.filter(is_delete=False, is_audit=1)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, context={'request': request})
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        # 修改文章
        instance = self.get_object()
        if instance.user != request.user:
            return Response({'message': '不能修改其他用户的文章'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({'message': '修改成功'}, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        # 删除文章
        instance = self.get_object()
        if instance.user != request.user:
            return Response({'message': '不能删除其他用户的文章'}, status=status.HTTP_400_BAD_REQUEST)
        instance.is_delete = True
        instance.save()
        return Response({'message': '删除成功'}, status=status.HTTP_200_OK)

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

# 对帖子浏览，使用GenericViewSet和mixins.RetrieveModelMixin, mixins.DestroyModelMixin,mixins.UpdateModelMixin
# 由帖子点赞就在ArticleLike表中创建一条记录，取消点赞就删除一条记录
class ArticleLikeGenericViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    permission_classes = [IsAuthenticated]
    serializer_class = ArticleLikeSerializer
    def create(self, request, *args, **kwargs):
        # 点赞,文章的pk从请求接口中获取，api/article/article-likes/2/
        # 文章的pk是2
        data= {
            'user': request.user.id,
            'article': kwargs.get('pk')
        }
        # 判断是否已经点赞
        try:
            ArticleLike.objects.get(user=request.user, article=kwargs.get('pk'))
            return Response({'message': '已经点赞'}, status=status.HTTP_400_BAD_REQUEST)
        except:
            pass
        serializer = ArticleLikeSerializer(data=data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': '点赞成功'}, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        try:
            article_like = ArticleLike.objects.get(user=request.user, article=kwargs.get('pk'))
            article_like.delete()
            return Response({'message': '取消点赞成功'}, status=status.HTTP_200_OK)
        except:
            return Response({'message': '取消点赞失败'}, status=status.HTTP_400_BAD_REQUEST)

# 对帖子浏览，使用GenericViewSet,mixins.UpdateModelMixin
# 由帖子浏览就在ArticleView表中创建一条记录
class ArticleViewGenericViewSet(viewsets.GenericViewSet, mixins.UpdateModelMixin):
    permission_classes = [IsAuthenticated]
    serializer_class = ArticleViewSerializer
    def update(self, request, *args, **kwargs):
        # 浏览,文章的pk从请求接口中获取，api/article/article-views/2/
        # 文章的pk是2
        data= {
            'user': request.user.id,
            'article': kwargs.get('pk')
        }
        # 判断是否已经浏览，已经浏览就修改浏览时间update_time
        try:
            article_view = ArticleView.objects.get(user=request.user, article=kwargs.get('pk'))
            article_view.save()
            return Response({'message': '浏览成功'}, status=status.HTTP_200_OK)
        except:
            pass
        serializer = self.get_serializer(data=data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': '浏览成功'}, status=status.HTTP_200_OK)

# 根据文章的pk查询文章的评论和回复
class ArticleCommentGenericViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    permission_classes = [IsAuthenticated]
    serializer_class = ArticleCommentSerializer
    # 实现分页
    pagination_class = ArticlePagination

    def get_queryset(self):
        # 获取文章的pk
        article_pk = self.kwargs.get('pk')
        # 查询文章的评论
        article_comments = ArticleComment.objects.filter(article=article_pk, parent=None, is_audit=1, is_delete=False).order_by('-create_time')
        return article_comments


    def list(self, request, *args, **kwargs):
        # 查询文章的评论
        article_comments = self.get_queryset()
        # 分页
        page = self.paginate_queryset(article_comments)
        if page is not None:
            serializer = self.get_serializer(page, many=True, context={'request': request})
            return self.get_paginated_response(data=serializer.data)
        # 序列化
        serializer = self.get_serializer(article_comments, many=True, context={'request': request})
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        # 判断是否开启审核
        app_config = AppConfiguration.objects.first()
        if app_config.app_comment_audit == True:
            is_audit = 0
        else:
            is_audit = 1
        # 创建评论
        data = {
            'user': request.user.id,
            'article': kwargs.get('pk'),
            'content': request.data.get('content'),
            'parent': request.data.get('parent'),
            'is_anonymous': request.data.get('is_anonymous'),
            'is_audit': is_audit
        }
        serializer = ArticleCommentCreateSerializer(data=data, context={'request': request})
        serializer.is_valid(raise_exception=True)   # 校验数据
        serializer.save()
        return Response({'message': is_audit == 0 and '评论成功，等待审核' or '评论成功'}, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        # 查询评论的回复
        # 获取评论的pk
        comment_pk = self.kwargs.get('pk')
        # 查询评论的回复
        article_comments = ArticleComment.objects.filter(parent=comment_pk, is_audit=1, is_delete=False).order_by('-create_time')
        # 序列化
        serializer = self.get_serializer(article_comments, many=True, context={'request': request})
        return Response(serializer.data)


