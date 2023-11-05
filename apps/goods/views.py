from django.shortcuts import render
from rest_framework import mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.goods.models import GoodsGroup, GoodsBanner, Goods, GoodsCollection
from apps.goods.serializer import GoodsGroupSerializer, GoodsBannerSerializer, GoodsSerializer, \
    GoodsCollectionSerializer

from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet

from common.permissions import IsAddressPermissions

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
        # 1.2 商品轮播图
        banners = GoodsBanner.objects.filter(status=True)
        # 1.3 商品推荐
        recommends = Goods.objects.filter(recommend=True, is_on_sale=True)
        # 1.4 商品列表
        goods = Goods.objects.filter(is_on_sale=True)
        # 序列化
        groups_data = GoodsGroupSerializer(groups, many=True).data
        banners_data = GoodsBannerSerializer(banners, many=True).data
        recommends_data = GoodsSerializer(recommends, many=True).data
        goods_data = GoodsSerializer(goods, many=True).data
        return Response({
            'groups': groups_data,
            'banners': banners_data,
            'recommends': recommends_data,
            'goods': goods_data
        })

class GoodsView(ReadOnlyModelViewSet):
    queryset = Goods.objects.filter(is_on_sale=True)
    serializer_class = GoodsSerializer
    filterset_fields = ['group', 'recommend']
    ordering_fields = ['price', 'sales']

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.sales += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class GoodsCollectionView(GenericViewSet,
                    mixins.CreateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.ListModelMixin):
    queryset = GoodsCollection.objects.all()
    serializer_class = GoodsCollectionSerializer
    filterset_fields = ['user']
    permission_classes = [IsAuthenticated,IsAddressPermissions]

    def create(self, request, *args, **kwargs):
        user = request.user
        params_user_id = request.data.get('user')
        if user.id != int(params_user_id):
            return Response({'error': '没有权限'}, status=status.HTTP_400_BAD_REQUEST)
        # 判断是否已经收藏
        goods_id = request.data.get('goods')
        if GoodsCollection.objects.filter(user=user, goods_id=goods_id).exists():
            return Response({'error': '已经收藏'}, status=status.HTTP_400_BAD_REQUEST)

        return super().create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(user=request.user)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

