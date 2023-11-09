from django.core.mail import send_mail

def send_email(subject, message, from_email, recipient_list):
    try:
        send_mail(
            subject,
            message,
            from_email,
            recipient_list,
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