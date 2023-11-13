from rest_framework import serializers
from .models import Article, ArticleComment, ArticleLike, ArticleView, ArticleFile

class ArticleFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleFile
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    files = ArticleFileSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = '__all__'

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
