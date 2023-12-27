from django.apps import AppConfig


class BookManageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.book_manage'
    verbose_name = '图书管理系统'