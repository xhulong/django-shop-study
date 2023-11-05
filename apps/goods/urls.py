from django.urls import path
from apps.goods import views
urlpatterns = [
    # 首页数据获取
    path('index/', views.IndexView.as_view(), name='index'),
    # 商品列表
    path('list/', views.GoodsView.as_view({'get': 'list'}), name='goods'),
    # 商品详情
    path('detail/<int:pk>/', views.GoodsView.as_view({'get': 'retrieve'}), name='goods'),
    # 商品收藏和获取收藏列表
    path('collection/', views.GoodsCollectionView.as_view({'post': 'create', 'get': 'list'}), name='collection'),
    # 商品取消收藏
    path('collection/<int:pk>/', views.GoodsCollectionView.as_view({'delete': 'destroy'}), name='collection'),
]