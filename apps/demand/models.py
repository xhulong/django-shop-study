from django.db import models
from common.db import BaseModel

class Task(BaseModel):
    STATUS_CHOICES = (
        ('open', '正常'),
        ('closed', '关闭'),
        ('expired', '过期'),
    )

    TYPE_CHOICES = (
        ('delivery', '代取快递'),
        ('errand', '跑腿'),
    )

    title = models.CharField(max_length=100, verbose_name='任务标题', help_text='任务标题')
    description = models.TextField(verbose_name='任务描述', help_text='任务描述')
    type = models.CharField(max_length=50, choices=TYPE_CHOICES, verbose_name='任务类型', help_text='任务类型')
    creator = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name='创建者', help_text='创建者')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='open', verbose_name='状态', help_text='状态')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间', help_text='创建时间')
    # 任务佣金
    commission = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='佣金', help_text='佣金', default=0.00)
    # 备注
    remark = models.TextField(verbose_name='备注', help_text='备注', null=True, blank=True)
    # 任务截至时间
    deadline = models.DateTimeField(verbose_name='截至时间', help_text='截至时间', null=True, blank=True)
    class Meta:
        verbose_name = '任务'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class DeliveryTask(BaseModel):
    # 包裹大小
    PACKAGE_SIZE_CHOICES = [
        ('small', '小件'),
        ('medium', '中件'),
        ('large', '大件')
    ]

    # 期望送达时间，不限制，尽快送达，今天中午12点前，今天下午6点前，今天晚上10点前，其他时间请备注
    EXPECTED_TIME_CHOICES = [
        ('unlimited', '不限制'),
        ('asap', '尽快送达'),
        ('today_12', '今天中午12点前'),
        ('today_18', '今天下午6点前'),
        ('today_22', '今天晚上10点前'),
        ('other', '其他时间请备注'),
    ]
    # 性别要求, 男，女，不限制
    GENDER_CHOICES = [
        ('unlimited', '不限制'),
        ('man', '男'),
        ('girl', '女'),
    ]

    task = models.OneToOneField(Task, on_delete=models.CASCADE, verbose_name='任务', help_text='任务')
    package_size = models.CharField(max_length=50, choices=PACKAGE_SIZE_CHOICES, verbose_name='包裹大小', help_text='包裹大小')
    # 取件信息图片
    package_image = models.ImageField(upload_to='delivery', null=True, blank=True, verbose_name='取件信息图片', help_text='取件信息图片')
    # 取件信息
    package_info = models.CharField(max_length=200, verbose_name='取件信息', help_text='取件信息', null=True, blank=True)
    pickup_location = models.CharField(max_length=200, verbose_name='取件地点', help_text='取件地点', null=True, blank=True)
    # 期望送达时间
    expected_time = models.CharField(max_length=50, choices=EXPECTED_TIME_CHOICES, verbose_name='期望送达时间', help_text='期望送达时间', default='unlimited')
    # 性别要求
    gender = models.CharField(max_length=50,choices=GENDER_CHOICES, verbose_name='性别要求', help_text='性别要求', default='unlimited')

    class Meta:
        verbose_name = '代取快递任务'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.task.title


class ErrandTask(BaseModel):
    task = models.OneToOneField(Task, on_delete=models.CASCADE, verbose_name='任务', help_text='任务')
    start_location = models.CharField(max_length=200, verbose_name='开始地点', help_text='开始地点')
    end_location = models.CharField(max_length=200, verbose_name='结束地点', help_text='结束地点')


    class Meta:
        verbose_name = '跑腿任务'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.task.title


class TaskUser(BaseModel):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name='用户', help_text='用户')
    task = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name='任务', help_text='任务')
    accepted_at = models.DateTimeField(auto_now_add=True, verbose_name='接受时间', help_text='接受时间')

    class Meta:
        verbose_name = '任务接受者'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.username
