from django.contrib import admin
from apps.good.models import GoodsGroup, Goods

class FileInline(admin.TabularInline):
    model = Goods.images.through   # 通过中间表关联
    extra = 1   # 控制额外多几个
    verbose_name = '文件'
    verbose_name_plural = verbose_name

class GoodsGroupAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image', 'status']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'image', 'status']
    list_filter = ['name', 'image', 'status']
    list_per_page = 10

class GoodsAdmin(admin.ModelAdmin):
    inlines = [FileInline]
    list_display = ['id', 'group', 'title', 'desc', 'price', 'cover', 'stock', 'is_on_sale', 'recommend']
    list_display_links = ['id', 'title']
    search_fields = ['group', 'title', 'desc', 'price', 'cover', 'stock', 'is_on_sale', 'recommend']
    list_filter = ['group', 'title', 'desc', 'price', 'cover', 'stock', 'is_on_sale', 'recommend']
    list_per_page = 10




admin.site.register(GoodsGroup, GoodsGroupAdmin)
admin.site.register(Goods, GoodsAdmin)