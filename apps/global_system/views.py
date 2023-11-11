from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Message, Announcement, SiteConfiguration, WeChatConfiguration, QQConfiguration, EmailConfiguration, SMSConfiguration, QiniuConfiguration, AppConfiguration,IndexConfiguration,UserCenterConfiguration, Carousel
from .serializer import MessageSerializer, AnnouncementSerializer, SiteConfigurationSerializer, WeChatConfigurationSerializer, QQConfigurationSerializer, EmailConfigurationSerializer, SMSConfigurationSerializer, QiniuConfigurationSerializer, AppConfigurationSerializer,IndexConfigurationSerializer,UserCenterConfigurationSerializer, CarouselSerializer

# 查询app的所有配置
class AppConfigurationView(APIView):
    def get(self, request):
        # 1.查询app的所有配置
        app_config = AppConfiguration.objects.first()
        app_config_index = IndexConfiguration.objects.first()
        app_config_usercenter = UserCenterConfiguration.objects.first()
        # 2.序列化返回
        app_config_data = AppConfigurationSerializer(app_config, context={'request': request}).data
        app_config_index_data = IndexConfigurationSerializer(app_config_index, context={'request': request}).data
        app_config_usercenter_data = UserCenterConfigurationSerializer(app_config_usercenter, context={'request': request}).data
        # 查询首页轮播图
        # app_config_index_data里有index_carousel数组id
        # 通过id查询轮播图
        carousel_id = app_config_index_data['index_carousel']
        carousel = Carousel.objects.filter(id__in=carousel_id, is_delete=False, carousel_status=True)
        carousel_data = CarouselSerializer(carousel, many=True, context={'request': request}).data
        app_config_index_data['index_carousel'] = carousel_data
        data = {
            'app_config': app_config_data,
            'app_config_index': app_config_index_data,
            'app_config_usercenter': app_config_usercenter_data,
        }
        return Response({'data': data}, status=status.HTTP_200_OK)

# 查询系统的所有配置