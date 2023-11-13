from django.contrib import admin
from apps.user.models import User, Address, Area, VerifyCode
from django.contrib.auth.admin import UserAdmin
class UserInfoAdmin(UserAdmin):
    list_display = ['id','username', 'email', 'mobile', 'money', 'integral', 'avatar','last_name', 'sex','description', 'user_type', 'school', 'is_superuser'] # 显示字段
    list_display_links = ['id', 'username'] # 可以点击的字段
    search_fields = ['username', 'email', 'mobile', 'last_name', 'school']  # 搜索字段
    list_filter = ['username', 'email', 'mobile', 'last_name', 'school']    # 过滤字段
    list_per_page = 10
    ordering = ['id']   # 排序
    readonly_fields = ['money', 'integral', 'openid']  # 只读字段
    fieldsets = (None, {'fields': ('username', 'is_superuser', 'is_staff', 'is_active', 'school', 'email', 'mobile', 'money', 'integral', 'avatar', 'last_name', 'sex','user_type','description','groups', 'user_permissions')}),
    add_fieldsets = (None, {'classes': ('wide',), 'fields': (
    'username', 'password1', 'password2', 'school', 'mobile', 'is_superuser', 'is_staff', 'is_active', 'user_type', 'groups', 'user_permissions')}),
class AddressAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'phone', 'receiver', 'province', 'city', 'county', 'detail', 'is_default']
    list_display_links = ['id', 'user']
    search_fields = ['user', 'phone', 'receiver', 'province', 'city', 'county', 'detail', 'is_default']
    list_filter = ['user', 'phone', 'receiver', 'province', 'city', 'county', 'detail', 'is_default']
    list_per_page = 10

class AreaAdmin(admin.ModelAdmin):
    list_display = ['id', 'pid', 'name', 'level']
    list_display_links = ['id', 'pid']
    search_fields = ['pid', 'name', 'level']
    list_filter = ['pid', 'name', 'level']
    list_per_page = 10

class VerifyCodeAdmin(admin.ModelAdmin):
    list_display = ['id', 'code', 'mobile', 'create_time']
    list_display_links = ['id', 'code']
    search_fields = ['code', 'mobile', 'create_time']
    list_filter = ['code', 'mobile', 'create_time']
    list_per_page = 10

admin.site.register(User, UserInfoAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(VerifyCode, VerifyCodeAdmin)