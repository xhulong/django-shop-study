from django.urls import path
from apps.good import views
urlpatterns = [
    # 首页数据获取
    path('index/', views.IndexView.as_view(), name='index'),
    # 商品列表
    path('goods/', views.GoodsView.as_view({'get': 'list', 'post': 'create'}), name='goods'),
    # 商品详情
    path('detail/<int:pk>/', views.GoodsDetailView.as_view({'get': 'retrieve'}), name='detail'),
    # 商品收藏和获取收藏列表
    # 获取商分类
    path('group/', views.GoodsGroupView.as_view({'get': 'list'}), name='group'),
]