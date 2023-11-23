from rest_framework import serializers

from apps.file.models import FileSerializer
from apps.good.models import GoodsGroup, Goods, GoodsView
from apps.school.serializer import SchoolSerializer
from apps.user.serializer import UserSerializer


class GoodsGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsGroup
        fields = ['id', 'name', 'image']

class GoodsSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    school = SchoolSerializer()
    images = FileSerializer(many=True)

    class Meta:
        model = Goods
        fields = '__all__'

    # 只返回用户的头像和昵称
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['user'] = {
            'id': data['user']['id'],
            'username': data['user']['username'],
            'avatar': data['user']['avatar']
        }
        data['school'] = {
            'id': data['school']['id'],
            'name': data['school']['name'],
        }
        # 查询商品的浏览数
        data['view_count'] = GoodsView.objects.filter(good=data['id']).count()
        return data

# 创建商品，重新定义序列化器
class GoodsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = '__all__'
        extra_kwargs = {
            'user': {'required': True},
            'group': {'required': True},
            'school': {'required': True},
        }

class GoodsViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsView
        fields = '__all__'

