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
        # 查询前三条点赞的用户的头像和昵称
        like_all = ArticleLike.objects.filter(article=data['id'])
        # 如果没得点赞，就返回空列表
        if len(like_all) == 0:
            data['like_users'] = []
            data['is_like'] = False
            return data
        like_users_list = []
        for like in like_all:
            like_users_list.append(like.user)
        like_users = []
        for like_user in like_users_list:
            like_users.append({
                'id': like_user.id,
                'username': like_user.username,
                # request.build_absolute_uri()可以获取到当前请求的绝对路径
                'avatar': self.context['request'].build_absolute_uri(like_user.avatar.url)
            })
        data['like_users'] = like_users[:3]
        if self.context['request'].user.is_authenticated:
            try:
                ArticleLike.objects.get(user=self.context['request'].user, article=data['id'])
                data['is_like'] = True
            except:
                data['is_like'] = False
        else:
            data['is_like'] = False
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
    user = UserSerializer()
    class Meta:
        model = ArticleComment
        fields = ['id', 'content', 'user', 'article', 'parent', 'is_anonymous', 'create_time', 'is_audit', 'is_delete']

    # 给每个评论添加一个回复列表，并且只返回前三条回复，使用递归，评论模型有一个字段parent，用于表示父级评论
    def get_reply(self, parent_id):
        # 查询出所有的回复
        reply_all = ArticleComment.objects.filter(parent=parent_id)
        # 如果没有回复，就返回空列表
        if len(reply_all) == 0:
            return []
        reply_list = []
        for reply in reply_all:
            reply_list.append({
                'id': reply.id,
                'content': reply.content,
                'user': {
                    'id': reply.user.id,
                    'username': reply.user.username,
                    'avatar': self.context['request'].build_absolute_uri(reply.user.avatar.url)
                },
                'article': reply.article.id,
                'parent': reply.parent.id,
                'is_anonymous': reply.is_anonymous,
                'create_time': reply.create_time,
                'is_audit': reply.is_audit,
                'is_delete': reply.is_delete,
                'replyList': self.get_reply(reply.id)
            })
        return reply_list[:3]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['user'] = {
            'id': data['user']['id'],
            'username': data['user']['username'],
            'avatar': data['user']['avatar']
        }
        data['replyList'] = self.get_reply(data['id'])
        return data

# 重新写一个序列化器，用于创建评论
class ArticleCommentCreateSerializer(serializers.ModelSerializer):
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
