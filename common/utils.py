from django.core.mail import send_mail

def send_email(subject, message, from_email, recipient_list, html_message=None):
    try:
        send_mail(
            subject,          # 邮件标题
            message,          # 邮件内容（纯文本）
            from_email,       # 发件人
            recipient_list,   # 收件人列表
            html_message=html_message,  # 邮件内容（HTML）
            fail_silently=True,  # 如果邮件发送失败是否引发异常
        )
        return True  # 邮件发送成功
    except Exception as e:
        print("Error sending email:", str(e))
        return False  # 邮件发送失败

# 随机生成user+六位数字
def random_username():
    import random
    from apps.user.models import User
    while True:
        username = 'user' + str(random.randint(100000, 999999))
        if not User.objects.filter(username=username).exists():
            break
    return username


from apps.global_system.models import SiteConfiguration, WeChatConfiguration
# 获取系统配置信息，比如小程序appid等
class GetAppConfig:
    def __init__(self):
        self.app_config = SiteConfiguration.objects.first()
        self.wechat_config = WeChatConfiguration.objects.first()


    def get_app_config(self):
        return self.app_config

    def get_wechat_config(self):
        return self.wechat_config