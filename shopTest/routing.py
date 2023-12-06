# your_project/apps/user/routing.py
from django.urls import path, re_path

from apps.user.consumers import ChatConsumer


websocket_urlpatterns = [
    re_path(r'ws/(?P<group>\w+)/$', ChatConsumer.as_asgi()),
]
