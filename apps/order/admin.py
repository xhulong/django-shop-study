from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_no', 'order_status', 'order_amount', 'user', 'address', 'task')
    list_display_links = ['user', 'address', 'task']
    search_fields = ['order_no', 'order_status', 'user', 'address', 'task']
    list_filter = ['order_no', 'order_status', 'user', 'address', 'task']
    list_per_page = 10

admin.site.register(Order, OrderAdmin)
