from django.db import models

"""
学校模型
学校权限关联模型
学校配置模型

"""

class School(models.Model):
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

class SchoolUserPermissions(models.Model):
    """
    学校权限关联模型
    """
    PERMISSION_CHOICES = [
        (1, '超级管理员'),
        (2, '审核员'),
        (3, '运营人员')
    ]
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name='用户', help_text='用户')
    school = models.ForeignKey(School, on_delete=models.CASCADE, verbose_name='学校', help_text='学校')
    permission = models.IntegerField(choices=PERMISSION_CHOICES, default=1, verbose_name='权限', help_text='权限')
    is_disable = models.BooleanField(default=False, verbose_name='是否禁用', help_text='是否禁用')

    class Meta:
        db_table = 'ta_school_user_permissions'
        verbose_name = '学校权限关联'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.username

class SchoolConfig(models.Model):
    """
    学校配置模型
    存储JSON格式的数据
    """
    ACTIVITY_CHOICES = [
        (1, '图片模式'),
        (2, '图标模式')
    ]
    school = models.OneToOneField(School, on_delete=models.CASCADE, verbose_name='学校', help_text='学校')
    # home_title = models.CharField(max_length=20, verbose_name='首页标题', help_text='首页标题')
    # home_desc = models.CharField(max_length=50, verbose_name='首页描述', help_text='首页描述')
    # home_image = models.ImageField(upload_to='school/config', null=True, blank=True, verbose_name='首页图片', help_text='首页图片')
    # home_activity_image = models.ImageField(upload_to='school/config', null=True, blank=True, verbose_name='首页活动图片', help_text='首页活动图片')
    # home_activity_url = models.CharField(max_length=200, verbose_name='首页活动链接', help_text='首页活动链接')
    # home_activity_mode = models.IntegerField(choices=ACTIVITY_CHOICES, default=1, verbose_name='首页活动模式', help_text='首页活动模式')

    class Meta:
        db_table = 'ta_school_config'
        verbose_name = '学校配置'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.school.name