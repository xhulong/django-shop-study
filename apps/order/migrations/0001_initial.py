# Generated by Django 4.2.7 on 2023-11-20 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
            ],
            options={
                'verbose_name': '需求订单',
                'verbose_name_plural': '需求订单',
                'db_table': 'ta_order',
            },
        ),
    ]
