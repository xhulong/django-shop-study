from django.contrib import admin
from .models import Article, ArticleComment, ArticleLike, ArticleView, ArticleFile

class ArticleFileInline(admin.TabularInline):
    model = Article.files.through   # 通过中间表关联
    extra = 1   # 控制额外多几个

class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleFileInline]
    list_display = ('user', 'school', 'status', 'is_delete', 'is_top', 'is_hot', 'is_anonymous', 'is_audit', 'audit_user')

class ArticleCommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'user', 'article', 'parent', 'is_delete')

class ArticleLikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'article')

class ArticleViewAdmin(admin.ModelAdmin):
    list_display = ('user', 'article')

class ArticleFileAdmin(admin.ModelAdmin):
    list_display = ('file',)

admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleComment, ArticleCommentAdmin)
admin.site.register(ArticleLike, ArticleLikeAdmin)
admin.site.register(ArticleView, ArticleViewAdmin)
admin.site.register(ArticleFile, ArticleFileAdmin)
