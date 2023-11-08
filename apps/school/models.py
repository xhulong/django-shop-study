from django.db import models
from django.contrib.auth.models import Group
from common.db import BaseModel

"""
学校模型
学校权限关联模型

"""

class School(BaseModel):
    """
    学校模型
    """
    name = models.CharField(max_length=20, verbose_name='学校名称', help_text='学校名称')
    address = models.CharField(max_length=50, verbose_name='学校地址', help_text='学校地址')
    status = models.BooleanField(default=True, verbose_name='是否启用', help_text='是否启用')
    is_delete = models.BooleanField(default=False, verbose_name='是否删除', help_text='是否删除')

    class Meta:
        db_table = 'ta_school'
        verbose_name = '学校'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class SchoolUserPermissions(BaseModel):
    """
    学校权限关联模型
    """
    PERMISSION_CHOICES = [
        (1, '管理员'),
        (2, '审核员'),
        (3, '代理商')
    ]
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name='用户', help_text='用户')
    school = models.ForeignKey(School, on_delete=models.CASCADE, verbose_name='学校', help_text='学校')
    permission = models.IntegerField(choices=PERMISSION_CHOICES, default=3, verbose_name='权限', help_text='权限')
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, verbose_name='权限组', help_text='权限组')
    is_disable = models.BooleanField(default=False, verbose_name='是否禁用', help_text='是否禁用')

    class Meta:
        db_table = 'ta_school_user_permissions'
        verbose_name = '学校权限关联'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.username
