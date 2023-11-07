from django.contrib import admin
from .models import School, SchoolUserPermissions, SchoolConfig

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'address', 'status', 'is_delete']
    search_fields = ['name',]
    list_filter = ['status', 'is_delete']

@admin.register(SchoolUserPermissions)
class SchoolUserPermissionsAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'school', 'permission', 'is_disable']
    search_fields = ['user__username', 'school__name']
    list_filter = ['permission', 'is_disable']

@admin.register(SchoolConfig)
class SchoolConfigAdmin(admin.ModelAdmin):
    list_display = ['id', 'school', 'config']
    search_fields = ['school__name',]

admin.site.site_header = "XIAOO管理系统"
admin.site.site_title = "XIAOO管理系统"
