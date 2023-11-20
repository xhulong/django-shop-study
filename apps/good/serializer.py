from rest_framework import serializers
from apps.good.models import GoodsGroup, Goods

class GoodsGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsGroup
        fields = ['id', 'name', 'image', 'status']

class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = '__all__'

