from django.apps import AppConfig


class GlobalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.global_system'
    verbose_name = '全局管理'
