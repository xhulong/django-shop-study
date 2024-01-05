from django.db import models

# 学生信息管理系统，学生信息包括姓名、学号、电话、所属系等信息

class Student(models.Model):
    SEX_CHOICES = [
        (0, '男'),
        (1, '女')
    ]
    name = models.CharField(max_length=20, verbose_name='姓名')
    sno = models.CharField(max_length=20, verbose_name='学号')
    phone = models.CharField(max_length=20, verbose_name='电话')
    sex = models.IntegerField(choices=SEX_CHOICES, verbose_name='性别', default=1)
    address = models.CharField(max_length=20, verbose_name='地址')
    # 专业
    major = models.ForeignKey('Major', on_delete=models.SET_NULL, verbose_name='专业', null=True, blank=True)

    class Meta:
        db_table = 'student'
        verbose_name = '学生信息'
        verbose_name_plural = verbose_name


    def __str__(self):
        return self.name

# 系信息包括系名、系主任、系办公室电话等信息
class Department(models.Model):
    name = models.CharField(max_length=20, verbose_name='系名')
    director = models.CharField(max_length=20, verbose_name='系主任')
    phone = models.CharField(max_length=20, verbose_name='办公室电话')

    class Meta:
        db_table = 'department'
        verbose_name = '系信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

# 专业
class Major(models.Model):
    name = models.CharField(max_length=20, verbose_name='专业名')
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, verbose_name='所属系', null=True, blank=True)

    class Meta:
        db_table = 'major'
        verbose_name = '专业信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name