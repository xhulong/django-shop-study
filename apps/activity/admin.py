from django.contrib import admin
from .models import Activity, ActivityUser, ActivityBrowse

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'start_time', 'end_time', 'number_limit', 'creator', 'status', 'is_delete']
    search_fields = ['name', 'address', 'creator__username']
    list_filter = ['status', 'is_delete']

@admin.register(ActivityUser)
class ActivityUserAdmin(admin.ModelAdmin):
    list_display = ['user', 'activity', 'join_status', 'is_delete']
    search_fields = ['user__username', 'activity__name']
    list_filter = ['join_status', 'is_delete']

@admin.register(ActivityBrowse)
class ActivityBrowseAdmin(admin.ModelAdmin):
    list_display = ['user', 'activity', 'is_delete']
    search_fields = ['user__username', 'activity__name']
    list_filter = ['is_delete']
