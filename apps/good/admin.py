from django.contrib import admin
from apps.good.models import GoodsGroup, Goods, GoodsDetail, GoodsBanner, GoodsCollection

class GoodsGroupAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image', 'status']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'image', 'status']
    list_filter = ['name', 'image', 'status']
    list_per_page = 10

class GoodsAdmin(admin.ModelAdmin):
    list_display = ['id', 'group', 'title', 'desc', 'price', 'cover', 'stock', 'is_on_sale', 'recommend']
    list_display_links = ['id', 'title']
    search_fields = ['group', 'title', 'desc', 'price', 'cover', 'stock', 'is_on_sale', 'recommend']
    list_filter = ['group', 'title', 'desc', 'price', 'cover', 'stock', 'is_on_sale', 'recommend']
    list_per_page = 10

class GoodsDetailAdmin(admin.ModelAdmin):
    list_display = ['id', 'goods', 'producer', 'norms', 'detail']
    list_display_links = ['id', 'goods']
    search_fields = ['goods', 'producer', 'norms', 'detail']
    list_filter = ['goods', 'producer', 'norms', 'detail']
    list_per_page = 10

class GoodsBannerAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'image', 'seq', 'status']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'image', 'seq', 'status']
    list_filter = ['title', 'image', 'seq', 'status']
    list_per_page = 10

class GoodsCollectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'goods', 'user']
    list_display_links = ['id', 'goods']
    search_fields = ['goods', 'user']
    list_filter = ['goods', 'user']
    list_per_page = 10

admin.site.register(GoodsGroup, GoodsGroupAdmin)
admin.site.register(Goods, GoodsAdmin)
admin.site.register(GoodsDetail, GoodsDetailAdmin)
admin.site.register(GoodsBanner, GoodsBannerAdmin)
admin.site.register(GoodsCollection, GoodsCollectionAdmin)