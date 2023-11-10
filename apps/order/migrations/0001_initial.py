# Generated by Django 4.2.7 on 2023-11-09 02:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0001_initial'),
        ('demand', '0004_alter_task_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('order_status', models.CharField(choices=[('unpaid', '未支付'), ('pending', '待处理'), ('processing', '处理中'), ('completed', '已完成'), ('cancelled', '已取消')], default='unpaid', help_text='订单状态', max_length=50, verbose_name='订单状态')),
                ('order_no', models.CharField(help_text='订单编号', max_length=50, verbose_name='订单编号')),
                ('order_amount', models.DecimalField(decimal_places=2, help_text='订单金额', max_digits=10, verbose_name='订单金额')),
                ('remark', models.TextField(blank=True, help_text='订单备注', null=True, verbose_name='订单备注')),
                ('payment_method', models.CharField(blank=True, help_text='支付方式', max_length=50, null=True, verbose_name='支付方式')),
                ('address', models.ForeignKey(blank=True, help_text='地址', null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.address', verbose_name='地址')),
                ('task', models.ForeignKey(blank=True, help_text='任务', null=True, on_delete=django.db.models.deletion.SET_NULL, to='demand.task', verbose_name='任务')),
                ('user', models.ForeignKey(help_text='用户', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '订单',
                'verbose_name_plural': '订单',
                'db_table': 'ta_order',
            },
        ),
    ]