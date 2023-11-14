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
    files = serializers.FileField()

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
