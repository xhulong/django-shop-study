from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from common.db import BaseModel
from solo.models import SingletonModel

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

# 系统配置模型
class SiteConfiguration(SingletonModel):
    # 系统名称
    site_name = models.CharField(max_length=200, verbose_name='系统名称')
    # 系统LOGO
    site_logo = models.ImageField(upload_to='site/%Y/%m/%d/', verbose_name='系统LOGO', null=True, blank=True)
    # 系统描述
    site_description = models.TextField(verbose_name='系统描述', null=True, blank=True)
    # 系统备案号
    site_icp = models.CharField(max_length=200, verbose_name='系统备案号', null=True, blank=True)
    # 系统状态
    site_status = models.BooleanField(default=True, verbose_name='系统状态')

    class Meta:
        verbose_name = '系统配置'
        verbose_name_plural = '系统配置'

    def __str__(self):
        return self.site_name

# 微信配置
class WeChatConfiguration(SingletonModel):
    site_configuration = models.OneToOneField(SiteConfiguration, on_delete=models.CASCADE,
                                              related_name='wechat_configuration', verbose_name='关联的系统配置')
    # 微信支付
    # 微信支付商户号
    wechat_pay_mch_id = models.CharField(max_length=200, verbose_name='微信支付商户号', null=True, blank=True)
    # 微信支付API密钥
    wechat_pay_api_key = models.CharField(max_length=200, verbose_name='微信支付API密钥', null=True, blank=True)
    # 微信公众号名称
    wechat_name = models.CharField(max_length=200, verbose_name='微信公众号名称')
    # 微信公众号二维码
    wechat_qrcode = models.ImageField(upload_to='wechat/%Y/%m/%d/', verbose_name='微信公众号二维码', null=True, blank=True)
    # 微信公众号AppID
    wechat_appid = models.CharField(max_length=200, verbose_name='微信公众号AppID', null=True, blank=True)
    # 微信公众号AppSecret
    wechat_appsecret = models.CharField(max_length=200, verbose_name='微信公众号AppSecret', null=True, blank=True)
    # 微信公众号Token
    wechat_token = models.CharField(max_length=200, verbose_name='微信公众号Token', null=True, blank=True)
    # 小程序名字
    wechat_app_name = models.CharField(max_length=200, verbose_name='小程序名字', null=True, blank=True)
    # 小程序AppID
    wechat_app_appid = models.CharField(max_length=200, verbose_name='小程序AppID', null=True, blank=True)
    # 小程序AppSecret
    wechat_app_appsecret = models.CharField(max_length=200, verbose_name='小程序AppSecret', null=True, blank=True)

    class Meta:
        verbose_name = '微信配置'
        verbose_name_plural = '微信配置'

    def __str__(self):
        return self.wechat_name

# qq配置
class QQConfiguration(SingletonModel):
    site_configuration = models.OneToOneField(SiteConfiguration, on_delete=models.CASCADE,
                                              related_name='qq_configuration', verbose_name='关联的系统配置')
    # QQ登录
    # QQ登录APPID
    qq_appid = models.CharField(max_length=200, verbose_name='QQ登录APPID', null=True, blank=True)
    # QQ登录APPKEY
    qq_appkey = models.CharField(max_length=200, verbose_name='QQ登录APPKEY', null=True, blank=True)

    class Meta:
        verbose_name = 'QQ配置'
        verbose_name_plural = 'QQ配置'

    def __str__(self):
        return self.qq_appid

# 邮箱配置
class EmailConfiguration(SingletonModel):
    site_configuration = models.OneToOneField(SiteConfiguration, on_delete=models.CASCADE,
                                              related_name='email_configuration', verbose_name='关联的系统配置')
    # 邮箱配置
    # 邮箱服务器
    email_host = models.CharField(max_length=200, verbose_name='邮箱服务器', null=True, blank=True)
    # 邮箱端口
    email_port = models.CharField(max_length=200, verbose_name='邮箱端口', null=True, blank=True)
    # 发送邮件的邮箱
    email_host_user = models.CharField(max_length=200, verbose_name='发送邮件的邮箱', null=True, blank=True)
    # 在邮箱中设置的客户端授权密码
    email_host_password = models.CharField(max_length=200, verbose_name='在邮箱中设置的客户端授权密码', null=True, blank=True)
    # 是否使用了SSL或者TLS，为True时一般使用的是465端口，为False时一般使用的是25端口
    email_use_ssl = models.BooleanField(default=False, verbose_name='是否使用了SSL或者TLS')

    class Meta:
        verbose_name = '邮箱配置'
        verbose_name_plural = '邮箱配置'

    def __str__(self):
        return self.email_host

# 短信配置
class SMSConfiguration(SingletonModel):
    site_configuration = models.OneToOneField(SiteConfiguration, on_delete=models.CASCADE,
                                              related_name='sms_configuration', verbose_name='关联的系统配置')
    # 短信配置
    # 短信应用SDK AppID
    tencent_sms_app_id = models.CharField(max_length=200, verbose_name='短信应用SDK AppID', null=True, blank=True)
    # 短信应用SDK AppKey
    tencent_sms_app_key = models.CharField(max_length=200, verbose_name='短信应用SDK AppKey', null=True, blank=True)
    # 短信签名内容
    tencent_sms_sign = models.CharField(max_length=200, verbose_name='短信签名内容', null=True, blank=True)
    # 短信模板ID，需要在短信应用中申请
    tencent_sms_template_id = models.CharField(max_length=200, verbose_name='短信模板ID', null=True, blank=True)
    # 短信应用secretid
    tencent_sms_secretid = models.CharField(max_length=200, verbose_name='短信应用secretid', null=True, blank=True)
    # 短信应用secretkey
    tencent_sms_secretkey = models.CharField(max_length=200, verbose_name='短信应用secretkey', null=True, blank=True)


    class Meta:
        verbose_name = '短信配置'
        verbose_name_plural = '短信配置'

    def __str__(self):
        return self.tencent_sms_app_id

# 七牛云配置
class QiniuConfiguration(SingletonModel):
    site_configuration = models.OneToOneField(SiteConfiguration, on_delete=models.CASCADE,
                                              related_name='qiniu_configuration', verbose_name='关联的系统配置')
    # 七牛云配置
    # 七牛云AccessKey
    qiniu_access_key = models.CharField(max_length=200, verbose_name='七牛云AccessKey', null=True, blank=True)
    # 七牛云SecretKey
    qiniu_secret_key = models.CharField(max_length=200, verbose_name='七牛云SecretKey', null=True, blank=True)
    # 七牛云存储空间名称
    qiniu_bucket_name = models.CharField(max_length=200, verbose_name='七牛云存储空间名称', null=True, blank=True)
    # 七牛云存储空间域名
    qiniu_bucket_domain = models.CharField(max_length=200, verbose_name='七牛云存储空间域名', null=True, blank=True)
    # 是否使用七牛云存储
    qiniu_enable = models.BooleanField(default=False, verbose_name='是否使用七牛云存储')
    class Meta:
        verbose_name = '七牛云配置'
        verbose_name_plural = '七牛云配置'

    def __str__(self):
        return self.qiniu_access_key

# app配置模型
class AppConfiguration(SingletonModel):
    # app名称
    app_name = models.CharField(max_length=200, verbose_name='app名称')
    # app描述
    app_description = models.TextField(verbose_name='app描述', null=True, blank=True)
    # app状态
    app_status = models.BooleanField(default=True, verbose_name='app状态')
    # applogo
    app_logo = models.ImageField(upload_to='app/%Y/%m/%d/', verbose_name='applogo', null=True, blank=True)
    # 绑定手机号是否必须
    app_bind_phone = models.BooleanField(default=True, verbose_name='手机号是否必绑定')
    # 绑定邮箱是否必须
    app_bind_email = models.BooleanField(default=True, verbose_name='邮箱是否必绑定')
    # 帖子是否需要审核
    app_post_audit = models.BooleanField(default=True, verbose_name='帖子是否需要审核')
    # 活动是否需要审核
    app_activity_audit = models.BooleanField(default=True, verbose_name='活动是否需要审核')
    # 闲置是否需要审核
    app_idle_audit = models.BooleanField(default=True, verbose_name='闲置是否需要审核')

    class Meta:
        verbose_name = 'app配置'
        verbose_name_plural = 'app配置'

    def __str__(self):
        return self.app_name

# 首页配置模型
class IndexConfiguration(SingletonModel):
    # 和app一对一关联
    app_configuration = models.OneToOneField(AppConfiguration, on_delete=models.CASCADE,
                                              related_name='index_configuration', verbose_name='关联的app配置')
    # 首页轮播图
    index_carousel = models.ManyToManyField('global_system.Carousel', related_name='index_carousel', blank=True, verbose_name='首页轮播图')
    # 首页title
    index_title = models.CharField(max_length=200, verbose_name='首页title', null=True, blank=True)
    # 首页description
    index_description = models.TextField(verbose_name='首页description', null=True, blank=True)
    # 首页活动背景图
    index_activity_bg = models.ImageField(upload_to='index/%Y/%m/%d/', verbose_name='首页活动背景图', null=True, blank=True)
    # 首页闲置背景图
    index_idle_bg = models.ImageField(upload_to='index/%Y/%m/%d/', verbose_name='首页闲置背景图', null=True, blank=True)
    # 首页活动背景图
    index_demand_bg = models.ImageField(upload_to='index/%Y/%m/%d/', verbose_name='首页需求背景图', null=True, blank=True)
    # 首页需求发布背景图
    index_demand_publish_bg = models.ImageField(upload_to='index/%Y/%m/%d/', verbose_name='首页需求发布背景图', null=True, blank=True)
    # 首页ai背景图
    index_ai_bg = models.ImageField(upload_to='index/%Y/%m/%d/', verbose_name='首页ai背景图', null=True, blank=True)
    class Meta:
        verbose_name = '首页配置'
        verbose_name_plural = '首页配置'

    def __str__(self):
        return '首页配置'

# 个人中心配置模型
class UserCenterConfiguration(SingletonModel):
    # 和app一对一关联
    app_configuration = models.OneToOneField(AppConfiguration, on_delete=models.CASCADE,
                                              related_name='user_center_configuration', verbose_name='关联的app配置')
    # 个人vip标签是否显示
    user_center_vip = models.BooleanField(default=False, verbose_name='个人vip标签是否显示')
    # 个人钱包是否显示
    user_center_wallet = models.BooleanField(default=False, verbose_name='个人钱包是否显示')
    class Meta:
        verbose_name = '个人中心配置'
        verbose_name_plural = '个人中心配置'

    def __str__(self):
        return '个人中心配置'

# 轮播图模型
class Carousel(BaseModel):
    # 轮播图名称
    carousel_name = models.CharField(max_length=200, verbose_name='轮播图名称')
    # 轮播图图片
    carousel_image = models.ImageField(upload_to='carousel/%Y/%m/%d/', verbose_name='轮播图图片', null=True, blank=True)
    # 轮播图链接
    carousel_link = models.CharField(max_length=200, verbose_name='轮播图链接', null=True, blank=True)
    # 轮播图状态
    carousel_status = models.BooleanField(default=True, verbose_name='轮播图状态')
    # 轮播图排序
    carousel_order = models.IntegerField(default=0, verbose_name='轮播图排序')

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = '轮播图'

    def __str__(self):
        return self.carousel_name