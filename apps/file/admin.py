from django.contrib import admin
from .models import File

class FileInline(admin.ModelAdmin):
    model = File
    verbose_name = '文件'
    verbose_name_plural = verbose_name

admin.site.register(File, FileInline)
