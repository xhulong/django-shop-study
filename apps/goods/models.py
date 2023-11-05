from django.db import models
from common.db import BaseModel
from ckeditor.fields import RichTextField

# 商品分类
class GoodsGroup(BaseModel):
    name = models.CharField(max_length=20, verbose_name='分类名称', help_text='分类名称')
    image = models.ImageField(upload_to='goods/group', null=True, blank=True, verbose_name='分类图片', help_text='分类图片')
    status = models.BooleanField(default=True, verbose_name='是否显示', help_text='是否显示')

    class Meta:
        db_table = 'ta_goods_group'
        verbose_name = '商品分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

# 商品
class Goods(BaseModel):
    group = models.ForeignKey(GoodsGroup, on_delete=models.CASCADE, verbose_name='商品分类', help_text='商品分类')
    title = models.CharField(max_length=20, verbose_name='商品标题', help_text='商品标题')
    desc = models.CharField(max_length=50, verbose_name='商品描述', help_text='商品描述')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='商品价格', help_text='商品价格')
    cover = models.ImageField(upload_to='goods', null=True, blank=True, verbose_name='商品封面', help_text='商品封面')
    stock = models.IntegerField(default=0, verbose_name='商品库存', help_text='商品库存')
    sales = models.IntegerField(default=0, verbose_name='商品销量', help_text='商品销量')
    is_on_sale = models.BooleanField(default=True, verbose_name='是否上架', help_text='是否上架')
    recommend = models.BooleanField(default=False, verbose_name='是否推荐', help_text='是否推荐')

    class Meta:
        db_table = 'ta_goods'
        verbose_name = '商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

class GoodsDetail(BaseModel):
    goods = models.OneToOneField(Goods, on_delete=models.CASCADE, verbose_name='商品', help_text='商品')
    producer = models.CharField(max_length=20, verbose_name='生产厂家', help_text='生产厂家')
    norms = models.CharField(max_length=20, verbose_name='商品规格', help_text='商品规格')
    detail = RichTextField(verbose_name='商品详情', help_text='商品详情', null=True, blank=True)

    class Meta:
        db_table = 'ta_goods_detail'
        verbose_name = '商品详情'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name

# 商品轮播图
class GoodsBanner(BaseModel):
    title = models.CharField(max_length=20, verbose_name='轮播标题', help_text='轮播标题')
    # goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name='商品', help_text='商品')
    image = models.ImageField(upload_to='goods/banner', null=True, blank=True, verbose_name='商品轮播图', help_text='商品轮播图')
    seq = models.IntegerField(default=0, verbose_name='轮播顺序', help_text='轮播顺序')
    status = models.BooleanField(default=True, verbose_name='是否显示', help_text='是否显示')

    class Meta:
        db_table = 'ta_goods_banner'
        verbose_name = '商品轮播图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

# 商品收藏
class GoodsCollection(BaseModel):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name='用户', help_text='用户')
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name='商品', help_text='商品')

    class Meta:
        db_table = 'ta_goods_collection'
        verbose_name = '商品收藏'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.username



