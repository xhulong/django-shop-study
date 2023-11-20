from rest_framework import mixins, status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.good.models import GoodsGroup, Goods
from apps.good.serializer import GoodsGroupSerializer, GoodsSerializer

from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet


"""
商品模块前台接口
1.商城首页：
    1.1 商品分类
    1.2 商品轮播图
    1.3 商品推荐
    1.4 商品列表
2.点击商品
    展示商品详情
3.收藏商品
    3.1 收藏商品
    3.2 取消收藏
    3.3 收藏列表
4.分类获取商品列表
    4.1 支持分类获取商品列表
    4.2 获取推荐商品列表
    4.3 排序
"""

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

class GoodsView(ReadOnlyModelViewSet):
    queryset = Goods.objects.filter(is_on_sale=True)
    serializer_class = GoodsSerializer
    filterset_fields = ['group', 'recommend']
    ordering_fields = ['price', 'sales']

# 商品详情
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        result = serializer.data
        # 获取商品详情
        result['detail'] = instance.detail
        # 获取商品图片
        result['images'] = [image.image.url for image in instance.images.all()]
        return Response(result)



# 获取商品分类
class GoodsGroupView(mixins.ListModelMixin, GenericViewSet):
    queryset = GoodsGroup.objects.filter(status=True)
    serializer_class = GoodsGroupSerializer
