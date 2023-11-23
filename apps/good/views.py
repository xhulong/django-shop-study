from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.global_system.models import AppConfiguration
from apps.good.models import GoodsGroup, Goods
from apps.good.serializer import GoodsGroupSerializer, GoodsSerializer, GoodsCreateSerializer, GoodsViewSerializer

from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet
from rest_framework import status, viewsets, mixins

from common.permissions import IsOwnerOrReadOnly

"""
商品模块前台接口
1.商城首页：
    1.1 商品分类
    1.2 商品推荐
    1.3 商品列表
2.点击商品
    展示商品详情
3.分类获取商品列表
    3.1 支持分类获取商品列表
    3.2 获取推荐商品列表
    3.3 排序
"""
class GoodsPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    max_page_size = 100
class IndexView(APIView):
    def get(self, request):
        # 1.1 商品分类
        groups = GoodsGroup.objects.filter(status=True)
        # 1.3 商品推荐
        recommends = Goods.objects.filter(recommend=True, is_on_sale=True)
        # 1.4 商品列表
        goods = Goods.objects.filter(is_on_sale=True)
        # 序列化
        # 序列化如果有图片，返回数据需要补全完整得到图片路径，所以需要传入request
        groups_data = GoodsGroupSerializer(groups, many=True,context={'request': request}).data
        recommends_data = GoodsSerializer(recommends, many=True,context={'request': request}).data
        goods_data = GoodsSerializer(goods, many=True,context={'request': request}).data

        return Response({
            'groups': groups_data,
            'recommends': recommends_data,
            'good': goods_data
        })

class GoodsView(GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    pagination_class = GoodsPagination
    queryset = Goods.objects.filter(is_on_sale=True)
    serializer_class = GoodsSerializer
    filterset_fields = ['group', 'recommend']
    ordering_fields = ['price', 'recommend']

    def create(self, request, *args, **kwargs):
        app_config = AppConfiguration.objects.first()
        if eval(request.data.get('user')) != request.user.id:
            return Response({'message': '不能为其他用户发布闲置'}, status=status.HTTP_400_BAD_REQUEST)
        # 帖子是否需要审核
        if app_config.app_idle_audit == True:
            is_audit = False
            is_on_sale = False
            message = '发布成功，等待审核'
        else:
            is_audit = True
            message = '发布成功'
        mutable_data = request.data.copy()
        mutable_data['is_audit'] = is_audit
        mutable_data['is_on_sale'] = is_on_sale
        serializer = GoodsCreateSerializer(data=mutable_data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data) # 获取头部信息
        return Response({'message': message}, status=status.HTTP_200_OK, headers=headers)

class GoodsDetailView(GenericViewSet,mixins.RetrieveModelMixin):
    queryset = Goods.objects.filter(is_on_sale=True)
    serializer_class = GoodsSerializer

# 获取商品分类
class GoodsGroupView(mixins.ListModelMixin, GenericViewSet):
    queryset = GoodsGroup.objects.filter(status=True)
    serializer_class = GoodsGroupSerializer

# 浏览商品，如果记录存在则更新，不存在则创建
class GoodsViewView(mixins.CreateModelMixin, GenericViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer

    def create(self, request, *args, **kwargs):
        # 判断用户是否浏览过该商品
        user = request.user.id
        good = request.data.get('good')
        if GoodsView.objects.filter(user=user, good=good).exists():
            # 更新
            instance = GoodsView.objects.get(user=user, good=good)
            instance.save()
        else:
            # 创建
            serializer = GoodsViewSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
        return Response({'message': '浏览成功'}, status=status.HTTP_200_OK)