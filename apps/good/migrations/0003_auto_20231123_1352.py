# Generated by Django 3.2.23 on 2023-11-23 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('good', '0002_goodsview'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goods',
            name='status',
        ),
        migrations.AddField(
            model_name='goods',
            name='is_audit',
            field=models.BooleanField(default=True, help_text='是否审核', verbose_name='是否审核'),
        ),
    ]
