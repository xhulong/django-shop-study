from django.db import models
from common.db import BaseModel

"""
文章帖子模型
    可以上传多张图片
评论模型
收藏模型
浏览模型
"""
class ArticleFile(BaseModel):
    file = models.FileField(upload_to='article_files/', verbose_name='文件', help_text='文件')

    class Meta:
        db_table = 'ta_article_file'
        verbose_name = '帖子文件'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.file)

class Article(BaseModel):
    """
    文章帖子模型
    """
    # 审核状态
    AUDIT_STATUS_CHOICES = [
        (0, '未审核'),
        (1, '审核通过'),
        (2, '审核未通过')
    ]
    title = models.CharField(max_length=50, verbose_name='文章标题', help_text='文章标题')
    content = models.TextField(verbose_name='文章内容', help_text='文章内容')
    files = models.ManyToManyField(ArticleFile, verbose_name='文件', help_text='文件', related_name='articles', blank=True)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name='用户', help_text='用户',
                             related_name='user_articles', blank=False, null=False)
    school = models.ForeignKey('school.School', on_delete=models.CASCADE, verbose_name='学校', help_text='学校',
                               related_name='school_articles', blank=False, null=False)
    status = models.BooleanField(default=True, verbose_name='是否启用', help_text='是否启用')
    is_delete = models.BooleanField(default=False, verbose_name='是否删除', help_text='是否删除')
    is_top = models.BooleanField(default=False, verbose_name='是否置顶', help_text='是否置顶')
    is_hot = models.BooleanField(default=False, verbose_name='是否热门', help_text='是否热门')
    is_anonymous = models.BooleanField(default=False, verbose_name='是否匿名', help_text='是否匿名')
    is_audit = models.IntegerField(choices=AUDIT_STATUS_CHOICES, default=1, verbose_name='审核状态', help_text='审核状态')
    audit_user = models.ForeignKey('user.User', on_delete=models.SET_NULL, null=True, verbose_name='审核人', help_text='审核人', related_name='audit_articles')

    class Meta:
        db_table = 'ta_article'
        verbose_name = '文章帖子'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

class ArticleComment(BaseModel):
    """
    评论模型
    """
    content = models.TextField(verbose_name='评论内容', help_text='评论内容')
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name='用户', help_text='用户')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='文章', help_text='文章')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name='父级评论', help_text='父级评论')
    # 审核状态
    AUDIT_STATUS_CHOICES = [
        (0, '未审核'),
        (1, '审核通过'),
        (2, '审核未通过')
    ]
    is_audit = models.IntegerField(choices=AUDIT_STATUS_CHOICES, default=1, verbose_name='审核状态', help_text='审核状态')
    is_delete = models.BooleanField(default=False, verbose_name='是否删除', help_text='是否删除')

    class Meta:
        db_table = 'ta_article_comment'
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content

class ArticleLike(BaseModel):
    """
    点赞模型
    """
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name='用户', help_text='用户')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='文章', help_text='文章')

    class Meta:
        db_table = 'ta_article_like'
        verbose_name = '点赞'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.username

class ArticleView(BaseModel):
    """
    浏览模型
    """
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name='用户', help_text='用户')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='文章', help_text='文章')

    class Meta:
        db_table = 'ta_article_view'
        verbose_name = '浏览'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.username
