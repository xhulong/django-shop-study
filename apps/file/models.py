from django.db import models
from rest_framework import serializers


# 建立文件模型，用于存储各类文件

class File(models.Model):
    file = models.FileField(upload_to='%Y/%m/%d/', verbose_name='文件')
    class Meta:
        db_table = 'ta_file'
        verbose_name = '文件'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.file)

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['id', 'file']