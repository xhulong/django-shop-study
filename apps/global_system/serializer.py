from rest_framework import serializers
from .models import Message, Announcement, SiteConfiguration, WeChatConfiguration, QQConfiguration, EmailConfiguration, SMSConfiguration, QiniuConfiguration, AppConfiguration,IndexConfiguration,UserCenterConfiguration, Carousel

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'

class SiteConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteConfiguration
        fields = '__all__'

class WeChatConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeChatConfiguration
        fields = '__all__'

class QQConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = QQConfiguration
        fields = '__all__'

class EmailConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailConfiguration
        fields = '__all__'

class SMSConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SMSConfiguration
        fields = '__all__'

class QiniuConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = QiniuConfiguration
        fields = '__all__'

class AppConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppConfiguration
        fields = '__all__'

class IndexConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndexConfiguration
        fields = '__all__'

class UserCenterConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCenterConfiguration
        fields = '__all__'

class CarouselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carousel
        fields = ['id','carousel_name','carousel_image','carousel_link','carousel_status','carousel_order']