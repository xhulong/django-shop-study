from ckeditor.fields import RichTextField
from django.db import models
from common.db import BaseModel
"""
活动模型
参加活动的用户模型
浏览活动的用户模型
"""

class Activity(BaseModel):
    """
    活动模型
    """
    name = models.CharField(max_length=20, verbose_name='活动名称', help_text='活动名称')
    address = models.CharField(max_length=50, verbose_name='活动地址', help_text='活动地址')
    # 活动开始时间
    start_time = models.DateTimeField(verbose_name='活动开始时间', help_text='活动开始时间')
    # 活动结束时间
    end_time = models.DateTimeField(verbose_name='活动结束时间', help_text='活动结束时间')
    # 人数限制
    number_limit = models.IntegerField(verbose_name='人数限制', help_text='人数限制')
    # 创建者
    creator = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name='创建者', help_text='创建者')
    # 活动详情
    detail = RichTextField(verbose_name='活动详情', help_text='活动详情', null=True, blank=True)
    status = models.BooleanField(default=True, verbose_name='是否启用', help_text='是否启用')
    is_delete = models.BooleanField(default=False, verbose_name='是否删除', help_text='是否删除')

    class Meta:
        db_table = 'ta_activity'
        verbose_name = '活动'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class ActivityUser(BaseModel):
    """
    参加活动的用户模型
    """
    status = [
        (1, '审核中'),
        (2, '审核通过'),
        (3, '审核失败'),
        (4, '已取消'),
        (5, '禁止参加')
    ]
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name='用户', help_text='用户')
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, verbose_name='活动', help_text='活动')
    # 加入状态
    join_status = models.IntegerField(choices=status, default=1, verbose_name='加入状态', help_text='加入状态')
    is_delete = models.BooleanField(default=False, verbose_name='是否删除', help_text='是否删除')

    class Meta:
        db_table = 'ta_activity_user'
        verbose_name = '用户管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.username

class ActivityBrowse(BaseModel):
    """
    浏览活动的用户模型
    """
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name='用户', help_text='用户')
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, verbose_name='活动', help_text='活动')
    is_delete = models.BooleanField(default=False, verbose_name='是否删除', help_text='是否删除')

    class Meta:
        db_table = 'ta_activity_browse'
        verbose_name = '浏览管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.username
