from django.contrib import admin, messages
from rest_framework.exceptions import ValidationError

from .models import School, SchoolUserPermissions

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
    def save_model(self, request, obj, form, change):
        # 检查用户是否是超级管理员
        if obj.user.is_superuser:
            messages.error(request, '超级管理员的权限组不能被修改')
            raise ValidationError('超级管理员的权限组不能被修改')
        else:
            # 在保存SchoolUserPermissions对象之前，更新用户的权限组
            obj.user.groups.clear()
            if obj.group:
                obj.user.groups.add(obj.group)
            super().save_model(request, obj, form, change)



