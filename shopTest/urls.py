"""
URL configuration for shopTest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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
    path('api/upload/', FileUploadView.as_view(), name='upload'),
    path('api/upload/avatar/', FileView.as_view(), name='upload'),
    path('api/good/', include('apps.good.urls'), name='good'),
    # 全局配置
    path('api/global_system/', include('apps.global_system.urls'), name='global_system'),
]
