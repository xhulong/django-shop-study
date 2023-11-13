from datetime import datetime, timedelta
import pytz  # 导入pytz库

from django.db import models
from common.db import BaseModel
# Create your models here.

# 用户表继承django自带的User表
from django.contrib.auth.models import AbstractUser

class User(AbstractUser, BaseModel):
    """用户模型类"""
    SEX_CHOICES = [
        (0, '男'),
        (1, '女'),
        (2, '保密')
    ]
    # 用户客户端类型，小程序，h5，app
    USER_TYPE_CHOICES = [
        (0, '小程序'),
        (1, 'h5'),
        (2, 'app')
    ]
    mobile = models.CharField(max_length=11, verbose_name="手机号",null=True, blank=True)
    avatar = models.ImageField(verbose_name="用户头像", null=True, blank=True, upload_to="avatar")
    money = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="用户余额", default=0)
    integral = models.IntegerField(verbose_name="用户积分", default=0)
    # 性别
    sex = models.IntegerField(choices=SEX_CHOICES, verbose_name='性别', default=3)
    # 个性签名
    description = models.CharField(max_length=100, verbose_name='个性签名', null=True, blank=True)
    # openid
    openid = models.CharField(max_length=100, verbose_name='openid', null=True, blank=True)
    # 用户类型
    user_type = models.IntegerField(choices=USER_TYPE_CHOICES, verbose_name='用户类型', default=1)
    # 关联学校模型，一个用户只能关联一个学校
    school = models.ForeignKey('school.School', on_delete=models.SET_NULL, verbose_name='学校', null=True, blank=True)

    """用户模型类"""
    class Meta:
        db_table = "ta_user"
        verbose_name = "用户"
        verbose_name_plural = verbose_name

class Address(BaseModel):
    """地址模型类"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="所属账户")
    phone = models.CharField(max_length=11, verbose_name="联系电话")
    receiver = models.CharField(max_length=20, verbose_name="收件人")
    province = models.CharField(max_length=20, verbose_name="省份")
    city = models.CharField(max_length=20, verbose_name="城市")
    county = models.CharField(max_length=20, verbose_name="区县")
    detail = models.CharField(max_length=256, verbose_name="详细地址")
    is_default = models.BooleanField(default=False, verbose_name="是否默认")

    class Meta:
        db_table = "ta_address"
        verbose_name = "地址"
        verbose_name_plural = verbose_name

class Area(models.Model):
    """省市区"""
    pid = models.IntegerField(default=0, verbose_name="父级id")
    name = models.CharField(max_length=20, verbose_name="名称")
    level = models.IntegerField(default=1, verbose_name="级别")

    class Meta:
        db_table = "ta_area"
        verbose_name = "省市区"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

# 验证码
class VerifyCode(models.Model):
    """验证码"""
    code = models.CharField(max_length=10, verbose_name="验证码")
    mobile = models.CharField(max_length=20, verbose_name="账号")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def is_expired(self, expiration_minutes=5):
        """
        检查验证码是否已经过期
        :param expiration_minutes: 验证码的有效分钟数，默认为 5 分钟
        """
        now = datetime.now(pytz.UTC)  # 将now调整为UTC时区的offset-aware datetime

        expiration_time = self.create_time + timedelta(minutes=expiration_minutes)

        if now > expiration_time:
            return True
        else:
            return False
    class Meta:
        db_table = "ta_verifycode"
        verbose_name = "验证码"
        verbose_name_plural = verbose_name
        indexes = [
            models.Index(fields=['mobile',]),
        ]

    def __str__(self):
        return self.code