from rest_framework import serializers
from apps.goods.models import GoodsGroup, Goods, GoodsDetail, GoodsBanner, GoodsCollection

class GoodsGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsGroup
        fields = '__all__'

class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = '__all__'

class GoodsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsDetail
        fields = '__all__'

class GoodsBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsBanner
        fields = '__all__'

class GoodsCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCollection
        fields = '__all__'
