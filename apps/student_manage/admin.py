from django.contrib import admin

from .models import Student, Department, Major

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'address', 'phone', 'sno', 'sex', 'major']
    search_fields = ['name', 'sno', 'phone']

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'director', 'phone']
    search_fields = ['name', 'director', 'phone']

@admin.register(Major)
class MajorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'department']
    search_fields = ['name', 'department__name']