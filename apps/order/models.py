from django.db import models
from common.db import BaseModel

# Create your models here.
class Order(BaseModel):
    #订单状态，未支付，待处理，处理中，已完成，已取消
    STATUS_CHOICES = [
        ('unpaid', '未支付'),
        ('pending', '待处理'),
        ('processing', '处理中'),
        ('completed', '已完成'),
        ('cancelled', '已取消'),
    ]
    # 订单状态
    order_status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='unpaid', verbose_name='订单状态', help_text='订单状态')
    # 订单编号
    order_no = models.CharField(max_length=50, verbose_name='订单编号', help_text='订单编号')
    # 订单金额
    order_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='订单金额', help_text='订单金额')
    # 订单备注
    remark = models.TextField(verbose_name='订单备注', help_text='订单备注', null=True, blank=True)
    # 支付方式
    payment_method = models.CharField(max_length=50, verbose_name='支付方式', help_text='支付方式', null=True, blank=True)
    # 用户
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name='用户', help_text='用户')
    # 地址信息可以为空，如果为空，就是用户的默认地址
    address = models.ForeignKey('user.Address', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='地址', help_text='地址')
    # 任务
    task = models.ForeignKey('demand.Task', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='任务', help_text='任务')

    class Meta:
        db_table = 'ta_order'
        verbose_name = '需求订单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.order_no