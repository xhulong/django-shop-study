from django.contrib import admin
from .models import Task, DeliveryTask, ErrandTask, TaskUser

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'type', 'creator', 'status', 'created_at')

class DeliveryTaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'task', 'package_size', 'pickup_location')

class ErrandTaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'task', 'start_location', 'end_location')

class TaskUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'task', 'accepted_at')

admin.site.register(Task, TaskAdmin)
admin.site.register(DeliveryTask, DeliveryTaskAdmin)
admin.site.register(ErrandTask, ErrandTaskAdmin)
admin.site.register(TaskUser, TaskUserAdmin)
