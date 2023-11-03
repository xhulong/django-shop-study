"""
自定义用户登录认证，实现多字段登录
"""
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.contrib.auth import get_user_model
from rest_framework import serializers

class CustomBackend(ModelBackend):
    """
    自定义用户登录认证，实现多字段登录
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        """
        重写认证方法，实现多字段登录
        :param request:
        :param username:
        :param password:
        :param kwargs:
        :return:
        """
        try:
            # 通过Q对象实现多字段登录
            user = get_user_model().objects.get(Q(username=username)|Q(mobile=username)|Q(email=username))
        except get_user_model().DoesNotExist:
            raise serializers.ValidationError({'message': '用户不存在'})
        else:
            if user.check_password(password):
                return user
            else:
                raise serializers.ValidationError({'message': '密码错误'})
