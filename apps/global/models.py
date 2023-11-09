from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from common.db import BaseModel

"""
    1. 站内信模型
    2. 公告模型
    3. 轮播图模型
    4. 友情链接模型
    5. 热门搜索模型
    6. 系统配置模型
"""

class Message(BaseModel):
    sender = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='sent_messages', verbose_name='发送者')
    subject = models.CharField(max_length=200, verbose_name='主题')
    content = models.TextField(verbose_name='内容')

    # 接收人可以为个人或所有
    recipients = models.ManyToManyField('user.User', related_name='received_messages', blank=True, verbose_name='接收人')

    # 消息类型字段
    MESSAGE_TYPE_CHOICES = (
        ('like', '点赞'),
        ('comment', '评论'),
    )
    message_type = models.CharField(max_length=10, choices=MESSAGE_TYPE_CHOICES, verbose_name='消息类型')

    # 关联信息字段
    related_id = models.PositiveIntegerField(verbose_name='关联ID', null=True, blank=True)
    # 消息状态字段
    is_read = models.BooleanField(default=False, verbose_name='是否已读')

    def send_to_all(self):
        # 如果接收人为所有用户，你可以使用以下方法
        all_users = User.objects.all()
        for user in all_users:
            self.recipients.add(user)

    class Meta:
        verbose_name = '站内信'
        verbose_name_plural = '站内信'

    def __str__(self):
        return f"{self.subject} - {self.sender}"

# 公告模型
class Announcement(BaseModel):
    title = models.CharField(max_length=200, verbose_name='标题')
    content = models.TextField(verbose_name='内容')
    detail = RichTextField(verbose_name='公告详情', help_text='公告详情', null=True, blank=True)
    # 公告通知时间
    notice_time = models.DateTimeField(verbose_name='通知时间', null=True, blank=True)

    class Meta:
        verbose_name = '公告'
        verbose_name_plural = '公告'

    def __str__(self):
        return self.title
