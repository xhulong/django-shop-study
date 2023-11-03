from django.db import models
from common.db import BaseModel
# Create your models here.

# 用户表继承django自带的User表
from django.contrib.auth.models import AbstractUser

class User(AbstractUser, BaseModel):
    mobile = models.CharField(max_length=11, verbose_name="手机号",default="")
    avatar = models.ImageField(upload_to="avatar", verbose_name="用户头像", null=True, blank=True)
    money = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="用户余额", default=0)
    integral = models.IntegerField(verbose_name="用户积分", default=0)

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
    mobile = models.CharField(max_length=11, verbose_name="手机号")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    class Meta:
        db_table = "ta_verifycode"
        verbose_name = "验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code