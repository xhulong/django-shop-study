from django.contrib import admin
from apps.good.models import GoodsGroup, Goods, GoodsView


class FileInline(admin.TabularInline):
    model = Goods.images.through   # 通过中间表关联
    extra = 1   # 控制额外多几个
    verbose_name = '文件'
    verbose_name_plural = verbose_name

class GoodsGroupAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image', 'status' ,'school']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'image', 'status']
    list_filter = ['name', 'image', 'status']
    list_per_page = 10

class GoodsAdmin(admin.ModelAdmin):
    inlines = [FileInline]
    list_display = ['id', 'user', 'contact', 'school', 'group', 'title', 'desc', 'price', 'stock', 'is_on_sale', 'recommend', 'is_audit', 'is_delete', 'create_time', 'update_time']
    list_display_links = ['id', 'title']
    search_fields = ['group', 'title', 'desc', 'price', 'stock', 'is_on_sale', 'recommend']
    list_filter = ['group', 'title', 'desc', 'price', 'stock', 'is_on_sale', 'recommend']
    list_per_page = 10
    list_editable = ['is_on_sale', 'recommend', 'is_audit', 'is_delete']

class GoodsViewAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'good', 'create_time', 'update_time']
    list_display_links = ['id', 'user', 'good']
    search_fields = ['user', 'good']
    list_filter = ['user', 'good']
    list_per_page = 10




admin.site.register(GoodsGroup, GoodsGroupAdmin)
admin.site.register(Goods, GoodsAdmin)
admin.site.register(GoodsView, GoodsViewAdmin)