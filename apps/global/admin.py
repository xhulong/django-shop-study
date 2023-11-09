from django.contrib import admin
from .models import Message, Announcement

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

admin.site.register(Message, MessageAdmin)
admin.site.register(Announcement, AnnouncementAdmin)