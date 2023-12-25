from django.contrib import admin
from .models import Article, ArticleComment, ArticleLike, ArticleView
from apps.file.models import File
class ArticleFileInline(admin.TabularInline):
    model = Article.files.through   # 通过中间表关联
    extra = 1   # 控制额外多几个
    verbose_name = '文件'
    verbose_name_plural = verbose_name

class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleFileInline]
    list_display = ('content', 'user', 'school', 'status', 'is_delete', 'is_top', 'is_hot', 'is_anonymous', 'is_audit', 'audit_user')
    # 允许点击列头进行排序
    sortable_by = ('user', 'school', 'status', 'is_delete', 'is_top', 'is_hot', 'is_anonymous', 'is_audit', 'audit_user')
    # 筛选字段
    list_filter = ('user', 'school', 'status', 'is_delete', 'is_top', 'is_hot', 'is_anonymous', 'is_audit')
class ArticleCommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'user', 'article', 'parent', 'is_anonymous', 'is_audit', 'is_delete', 'create_time')

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
