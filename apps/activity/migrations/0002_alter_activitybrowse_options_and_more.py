# Generated by Django 4.2.7 on 2023-11-08 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activitybrowse',
            options={'verbose_name': '浏览管理', 'verbose_name_plural': '浏览管理'},
        ),
        migrations.AlterModelOptions(
            name='activityuser',
            options={'verbose_name': '用户管理', 'verbose_name_plural': '用户管理'},
        ),
    ]
