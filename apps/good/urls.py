from django.urls import path
from apps.good import views
urlpatterns = [
    # 首页数据获取
    path('index/', views.IndexView.as_view(), name='index'),
    # 商品列表
    path('goods/', views.GoodsViewList.as_view({'get': 'list', 'post': 'create'}), name='goods'),
    # 商品详情
    path('detail/<int:pk>/', views.GoodsDetailView.as_view({'get': 'retrieve'}), name='detail'),
    # 商品收藏和获取收藏列表
    # 获取商分类
    path('group/', views.GoodsGroupView.as_view({'get': 'list'}), name='group'),
    # 浏览商品
    path('view/', views.GoodsViewView.as_view({'post': 'create'}), name='view'),
    # 对自己发布的商品进行操作
    path('mygoods/', views.GoodsSelfView.as_view({'get': 'list'})),
    path('mygoods/<int:pk>/', views.GoodsSelfView.as_view({'put': 'update', 'delete': 'destroy'})),
    # 修改商品上下架状态
    path('onsale/<int:pk>/', views.GoodsOnSaleView.as_view({'put': 'update'})),
]