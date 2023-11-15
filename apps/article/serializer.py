from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Article, ArticleComment, ArticleLike, ArticleView, ArticleFile
from apps.user.serializer import UserSerializer
from ..school.serializer import SchoolSerializer


class ArticleFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleFile
        fields = ['id', 'file']

class ArticleSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    school = SchoolSerializer()
    files = ArticleFileSerializer(many=True)
    class Meta:
        model = Article
        fields = '__all__'
        extra_kwargs = {
            'user': {'required': True},
            'school': {'required': True},
        }
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
        # 查询文章的评论数
        data['comment_count'] = ArticleComment.objects.filter(article=data['id']).count()
        # 查询文章的点赞数
        data['like_count'] = ArticleLike.objects.filter(article=data['id']).count()
        # 查询文章的浏览数
        data['view_count'] = ArticleView.objects.filter(article=data['id']).count()
        # 查询前三条评论的用户的头像和昵称
        # comment_users = ArticleComment.objects.filter(article=data['id']).order_by('-create_time')[:3]
        # comment_users_list = []
        # for comment_user in comment_users:
        #     comment_users_list.append({
        #         'id': comment_user.user.id,
        #         'username': comment_user.user.username,
        #         'avatar': comment_user.user.avatar
        #     })
        # data['comment_users'] = comment_users_list

        return data


# 重新写一个序列化器，用于创建文章
class ArticleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        extra_kwargs = {
            'user': {'required': True},
            'school': {'required': True},
        }

class ArticleCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleComment
        fields = '__all__'

class ArticleLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleLike
        fields = '__all__'

class ArticleViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleView
        fields = '__all__'
