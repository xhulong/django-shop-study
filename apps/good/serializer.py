from rest_framework import serializers
from apps.good.models import GoodsGroup, Goods, GoodsBanner

class GoodsGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsGroup
        fields = '__all__'

class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = '__all__'

class GoodsBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsBanner
        fields = '__all__'

