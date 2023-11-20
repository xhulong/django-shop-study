from django.db import models
from common.db import BaseModel
from ckeditor.fields import RichTextField

# 商品分类
class GoodsGroup(BaseModel):
    name = models.CharField(max_length=20, verbose_name='分类名称', help_text='分类名称')
    image = models.ImageField(upload_to='good/group', null=True, blank=True, verbose_name='分类图片', help_text='分类图片')
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
    # 商品所属学校
    school = models.ForeignKey('school.School', on_delete=models.CASCADE, verbose_name='学校', help_text='学校')
    title = models.CharField(max_length=20, verbose_name='商品标题', help_text='商品标题')
    desc = models.CharField(max_length=50, verbose_name='商品描述', help_text='商品描述')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='商品价格', help_text='商品价格')
    cover = models.ImageField(upload_to='good', null=True, blank=True, verbose_name='商品封面', help_text='商品封面')
    images = models.ManyToManyField('file.File', verbose_name='商品图片', help_text='商品图片', blank=True)
    stock = models.IntegerField(default=0, verbose_name='商品库存', help_text='商品库存')
    is_on_sale = models.BooleanField(default=True, verbose_name='是否上架', help_text='是否上架')
    recommend = models.BooleanField(default=False, verbose_name='是否推荐', help_text='是否推荐')

    class Meta:
        db_table = 'ta_goods'
        verbose_name = '商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title




