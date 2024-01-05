from django.contrib import admin
from .models import Message, Announcement, Carousel, SiteConfiguration, WeChatConfiguration, QQConfiguration, EmailConfiguration, SMSConfiguration, QiniuConfiguration, AppConfiguration,IndexConfiguration,UserCenterConfiguration
from solo.admin import SingletonModelAdmin

class MessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'content', 'create_time', 'update_time')
    list_display_links = ['subject', 'content']
    search_fields = ['subject', 'content']
    list_filter = ['subject', 'content']
    list_per_page = 10

class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'detail', 'notice_time', 'create_time', 'update_time')
    list_display_links = ['title', 'content']
    search_fields = ['title', 'content']
    list_filter = ['title', 'content']
    list_per_page = 10

class WechatConfigurationInline(admin.StackedInline):
    model = WeChatConfiguration
    can_delete = False
    verbose_name_plural = '微信配置'
    extra = 0  # 默认显示两个空白表单

class QQConfigurationInline(admin.StackedInline):
    model = QQConfiguration
    can_delete = False
    verbose_name_plural = 'QQ配置'
    extra = 0  # 默认显示两个空白表单

class EmailConfigurationInline(admin.StackedInline):
    model = EmailConfiguration
    can_delete = False
    verbose_name_plural = '邮箱配置'
    extra = 0  # 默认显示两个空白表单

class SMSConfigurationInline(admin.StackedInline):
    model = SMSConfiguration
    can_delete = False
    verbose_name_plural = '短信配置'
    extra = 0  # 默认显示两个空白表单

class QiniuConfigurationInline(admin.StackedInline):
    model = QiniuConfiguration
    can_delete = False
    verbose_name_plural = '七牛云配置'
    extra = 0  # 默认显示两个空白表单

class SiteConfigurationAdmin(SingletonModelAdmin):
    inlines = [WechatConfigurationInline, QQConfigurationInline, EmailConfigurationInline, SMSConfigurationInline, QiniuConfigurationInline]

class IndexConfigurationAdmin(admin.StackedInline):
    model = IndexConfiguration
    can_delete = False
    verbose_name_plural = '首页配置'
    extra = 0  # 默认显示两个空白表单

class UserCenterConfigurationAdmin(admin.StackedInline):
    model = UserCenterConfiguration
    can_delete = False
    verbose_name_plural = '用户中心配置'
    extra = 0  # 默认显示两个空白表单
class AppConfigurationAdmin(SingletonModelAdmin):
    inlines = [IndexConfigurationAdmin, UserCenterConfigurationAdmin]

class CarouselAdmin(admin.ModelAdmin):
    list_display = ('carousel_name', 'carousel_image', 'carousel_link', 'carousel_status', 'carousel_order', 'create_time', 'update_time')
    list_display_links = ['carousel_name', 'carousel_image']
    search_fields = ['carousel_name', 'carousel_image']
    list_filter = ['carousel_name', 'carousel_image']
    list_per_page = 10

admin.site.register(Message, MessageAdmin)
admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(SiteConfiguration, SiteConfigurationAdmin)
admin.site.register(AppConfiguration, AppConfigurationAdmin)
admin.site.register(Carousel, CarouselAdmin)

admin.site.site_header = "小胡子图书管理系统"
admin.site.site_title = "小胡子图书管理系统"