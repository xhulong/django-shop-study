from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework.documentation import include_docs_urls

from apps.user.views import FileView, FileUploadView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('apps.user.urls'), name='user'),
    path('docs/', include_docs_urls(title='API接口文档', description='xxx描述')),
    # re_path(r'files/(.+?)/', FileView.as_view(), name='file'),
    re_path(r'files/(?P<path>.+)', FileView.as_view(), name='file'),
    # 文件上传
    path('api/upload/', FileUploadView.as_view(), name='upload'),   # 需要登录
    path('api/upload/file/', FileView.as_view(), name='upload'),  # 无需登录
    path('api/file/', include('apps.file.urls'), name='file'),
    path('api/good/', include('apps.good.urls'), name='good'),
    # 全局配置
    path('api/global_system/', include('apps.global_system.urls'), name='global_system'),
    # 学校列表
    path('api/school/', include('apps.school.urls'), name='school'),
    # 文章
    path('api/article/', include('apps.article.urls'), name='article'),
]
