from django.urls import path

from apps.user import views
from apps.user.views import LoginView,RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('login/', LoginView.as_view(), name='token_obtain_pair'),
    path('register/', RegisterView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_obtain_pair'),
    # 获取用户信息
    path('getUserInfo/', views.UserInfoView.as_view({'get': 'retrieve'}), name='user_info'),
    # 上传头像
    path('avatar/upload/<int:pk>/', views.UserInfoView.as_view({'post': 'upload_avatar'}), name='user_avatar_upload'),
    # 添加地址和获取地址
    path('address/', views.AddressView.as_view({'post': 'create','get': 'list'}), name='user_address_add'),
    # 删除地址和修改地址
    path('address/<int:pk>/', views.AddressView.as_view({'delete': 'destroy','put': 'update'}), name='user_address_delete'),
    # 设置默认地址
    path('address/default/<int:pk>/', views.AddressView.as_view({'put': 'set_default'}), name='user_address_default'),
    # 发送短信验证码
    path('ten_sms/', views.OperateTenSms.as_view(), name='ten_sms'),
    # 修改用户昵称
    path('update_userInfo/<int:pk>/', views.UserInfoView.as_view({'put': 'update_userInfo'}), name='user_nickname'),
    # 修改用户所属学校
    path('update_school/<int:pk>/', views.UserInfoView.as_view({'put': 'update_school'}), name='user_school'),
    # 修改用户密码
    path('password/', LoginView.as_view(), name='user_password'),
    # 发送邮箱
    path('email/send/', views.OperateEmail.as_view(), name='send_email'),
    path('bind_account/', views.UserInfoView.as_view({'put': 'bind_account'}), name='bind_account'),
    # 小程序登录
    path('Login_capLogin/', views.MiniWechatLogin.as_view(), name='wx_login'),
    # ChatGPT
    path('chat/', views.OperateXunFei.as_view(), name='chat'),
]