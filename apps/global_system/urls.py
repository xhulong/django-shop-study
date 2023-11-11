from django.urls import path
from .views import AppConfigurationView
urlpatterns = [
    # app配置
    path('app/', AppConfigurationView.as_view(), name='app'),
]