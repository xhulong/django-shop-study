# Generated by Django 4.2.7 on 2023-11-17 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_remove_article_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlecomment',
            name='is_anonymous',
            field=models.BooleanField(default=False, help_text='是否匿名', verbose_name='是否匿名'),
        ),
    ]
