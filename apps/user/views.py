import os
import re
import random

import requests
from django.conf import settings
from django.http import FileResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from rest_framework import status, mixins, serializers
from rest_framework.decorators import permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.school.models import School
from apps.user.models import User, Address, VerifyCode
from apps.user.serializer import UserSerializer, AddressSerializer
from common import SparkApi
from common.permissions import IsAddressPermissions,IsOwnerOrReadOnly
from common.tencent_sms import SendTenSms
from common.utils import send_email,random_username



# Create your views here.

# 重写登录方法
class LoginView(TokenObtainPairView):
    def post(self, request: Request, *args, **kwargs) -> Response:
        response = super().post(request, *args, **kwargs)

        if response.status_code == status.HTTP_200_OK:
            result = response.data
            data = {
                'message': '登录成功',
                'data': {
                    'token': result['access'],
                    'refresh': result['refresh'],
                }
            }
            response.data = data

        return response
    #修改密码
    def put(self, request, *args, **kwargs):
        # 获取参数
        data = request.data
        phone = data.get('phone')
        password = data.get('password')
        code = data.get('code')
        if all([phone, password]) is False:
            return Response({'message': '参数不完整'}, status=status.HTTP_400_BAD_REQUEST)
        if len(password) < 6:
            return Response({'message': '密码长度不能小于6位'}, status=status.HTTP_400_BAD_REQUEST)
        # 校验验证码是否正确
        try:
            verify_code = VerifyCode.objects.get(mobile=phone, code=code)
            # 校验验证码是否过期
            if verify_code.is_expired(expiration_minutes=5):
                return Response({'message': '验证码过期'}, status=status.HTTP_400_BAD_REQUEST)
        except VerifyCode.DoesNotExist:
            return Response({'message': '验证码错误'}, status=status.HTTP_400_BAD_REQUEST)
        # 校验用户是否存在
        if User.objects.filter(mobile=phone).exists():
            user = User.objects.get(mobile=phone)
            user.set_password(password)
            user.save()
            # 删除验证码
            VerifyCode.objects.filter(mobile=phone).delete()
            return Response({
                'message': '修改成功'
            }, status=status.HTTP_200_OK)
        else:
            return Response({'message': '用户不存在'}, status=status.HTTP_400_BAD_REQUEST)

# 注册
class RegisterView(APIView):
    def post(self, request):
        # 获取参数
        data = request.data
        username = data.get('username')
        password = data.get('password')
        code = data.get('code')
        if all([username, password]) is False:
            return Response({'message': '参数不完整'}, status=status.HTTP_400_BAD_REQUEST)
        if len(password) < 6:
            return Response({'message': '密码长度不能小于6位'}, status=status.HTTP_400_BAD_REQUEST)
        # 校验验证码是否正确
        try:
            verify_code = VerifyCode.objects.get(mobile=username, code=code)
            # 校验验证码是否过期
            if verify_code.is_expired(expiration_minutes=5):
                return Response({'message': '验证码过期'}, status=status.HTTP_400_BAD_REQUEST)
        except VerifyCode.DoesNotExist:
            return Response({'message': '验证码错误'}, status=status.HTTP_400_BAD_REQUEST)
        # 校验用户是否存在
        if User.objects.filter(username=username).exists():
            return Response({'message': '用户已存在'}, status=status.HTTP_400_BAD_REQUEST)
        # 保存用户

        user = User.objects.create_user(username=random_username(), password=password, mobile=username, user_type=1)
        # 删除验证码
        VerifyCode.objects.filter(mobile=username).delete()
        # 返回用户信息
        return Response({
            'message': '注册成功'
        }, status=status.HTTP_201_CREATED)

# 获取用户信息
class UserInfoView(GenericViewSet,mixins.RetrieveModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]
    def retrieve(self, request, *args, **kwargs):
        user = request.user
        serializer = self.get_serializer(user)
        return Response(serializer.data)
    # 上传头像
    def upload_avatar(self, request, *args, **kwargs):
        obj = self.get_object()
        avatar = request.FILES.get('file')
        if not avatar:
            return Response({'message': '请选择图片'}, status=status.HTTP_400_BAD_REQUEST)
        size = avatar.size
        if size > 1024 * 1024 * 2:
            return Response({'message': '图片过大'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(obj, data={'avatar': avatar}, partial=True)
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save()
            # 数据保存成功，可以执行其他操作
        except Exception as e:
            return Response({'message': '上传失败'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': '上传成功', 'avatar': serializer.data['avatar']}, status=status.HTTP_200_OK)

    # 修改用户信息，username,sex,description
    def update_userInfo(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)   # 为True时，允许部分更新
        instance = self.get_object()
        # 从请求数据中提取仅允许更新的字段
        data_to_update = {k: v for k, v in request.data.items() if k in ['username', 'sex', 'description']}
        serializer = self.get_serializer(instance, data=data_to_update, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': '修改成功'}, status=status.HTTP_200_OK)
    # 修改用户所属学校
    def update_school(self, request, *args, **kwargs):
        instance = self.get_object()
        school_id = request.data.get('school_id')
        school = get_object_or_404(School, id=school_id)
        # 判断学校是否被禁用
        if school.status is False:
            return Response({'message': '学校已被禁用'}, status=status.HTTP_400_BAD_REQUEST)
        # 修改用户所属学校
        instance.school = school
        instance.save()
        return Response({'message': '修改成功'}, status=status.HTTP_200_OK)


    """
    绑定手机邮箱，解绑手机邮箱
    account: 账号
    code: 验证码
    type: 类型，mobile, email
    status: 1 绑定，2 更改，3 解绑
    """
    def bind_account(self, request, *args, **kwargs):
        account = request.data.get('account')
        code = request.data.get('code')
        type = request.data.get('type')
        status_account = request.data.get('status')
        # 转为数字
        type = int(type)
        status_account = int(status_account)
        # 校验验证码
        result = self.verif_code(account, code)
        if result is not None:
            return result
        # 判断用户是否已绑定
        obj = request.user
        if type == 1:
            # 判断status
            if status_account == 1:
                if obj.mobile is not None and obj.mobile != "":
                    return Response({'message': '用户已绑定'}, status=status.HTTP_400_BAD_REQUEST)
                obj.mobile = account
            elif status_account == 2:
                if obj.mobile is None or obj.mobile == "":
                    return Response({'message': '用户未绑定'}, status=status.HTTP_400_BAD_REQUEST)
                obj.mobile = account
            elif status_account == 3:
                if obj.mobile != account:
                    return Response({'message': '手机号不正确'}, status=status.HTTP_400_BAD_REQUEST)
                obj.mobile = ""
        elif type == 2:
            if status_account == 1:
                if obj.email is not None and obj.email != "":
                    return Response({'message': '用户已绑定'}, status=status.HTTP_400_BAD_REQUEST)
                obj.email = account
            elif status_account == 2:
                if obj.email is None or obj.email == "":
                    return Response({'message': '用户未绑定'}, status=status.HTTP_400_BAD_REQUEST)
                obj.email = account
            elif status_account == 3:
                if obj.email != account:
                    return Response({'message': '邮箱不正确'}, status=status.HTTP_400_BAD_REQUEST)
                obj.email = ""
        obj.save()
        # 删除验证码
        VerifyCode.objects.filter(mobile=account).delete()
        return Response({'message': '操作成功'}, status=status.HTTP_200_OK)


    # 封装验证码
    @staticmethod
    def verif_code(mobile, code):
        if not all([mobile, code]):
            return Response({'message': '参数不完整'}, status=status.HTTP_400_BAD_REQUEST)
        # 校验验证码 通过返回none，不通过返回对象
        try:
            verify_code = VerifyCode.objects.get(mobile=mobile, code=code)
            # 校验验证码是否过期
            if verify_code.is_expired(expiration_minutes=5):
                return Response({'message': '验证码过期'}, status=status.HTTP_400_BAD_REQUEST)
        except VerifyCode.DoesNotExist:
            return Response({'message': '验证码错误'}, status=status.HTTP_400_BAD_REQUEST)
        return None





# 文件访问
class FileView(APIView):
    def get(self, request, path):
        file_path = os.path.join(settings.MEDIA_ROOT, path)
        if os.path.exists(file_path):
            return FileResponse(open(file_path, 'rb'))
        else:
            return Response({'message': '文件不存在'}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        file = request.FILES.get('file')
        if not file:
            return Response({'message': '请选择文件'}, status=status.HTTP_400_BAD_REQUEST)
        size = file.size
        if size > 1024 * 1024 * 2:
            return Response({'message': '文件过大'}, status=status.HTTP_400_BAD_REQUEST)

        # 自定义上传路径
        upload_path = 'user/'
        file_path = os.path.join(settings.MEDIA_ROOT, upload_path, file.name)

        with open(file_path, 'wb') as f:
            for chunk in file.chunks():
                f.write(chunk)
                # 获取相对路径
                relative_path = os.path.join(upload_path, file.name)

                # 构建完整的URL
                full_url = request.build_absolute_uri(settings.MEDIA_URL + relative_path)

                return Response({'message': '上传成功', 'file_path': full_url, 'file': relative_path},
                                status=status.HTTP_200_OK)


# 文件上传
class FileUploadView(APIView):
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]
    def post(self, request):
        file = request.FILES.get('file')
        if not file:
            return Response({'message': '请选择文件'}, status=status.HTTP_400_BAD_REQUEST)
        size = file.size
        if size > 1024 * 1024 * 2:
            return Response({'message': '文件过大'}, status=status.HTTP_400_BAD_REQUEST)

        # 自定义上传路径
        upload_path = 'user/'
        file_path = os.path.join(settings.MEDIA_ROOT, upload_path, file.name)

        with open(file_path, 'wb') as f:
            for chunk in file.chunks():
                f.write(chunk)
                # 获取相对路径
                relative_path = os.path.join(upload_path, file.name)

                # 构建完整的URL
                full_url = request.build_absolute_uri(settings.MEDIA_URL + relative_path)

                return Response({'message': '上传成功', 'file_path': full_url},
                                status=status.HTTP_200_OK)


# 获取用户地址
class AddressView(GenericViewSet,
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated, IsAddressPermissions]

    # 重写list方法
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(user=request.user)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            # 获取用户地址
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    # 设置默认地址
    def set_default(self, request, *args, **kwargs):
        # 获取地址
        address = self.get_object()
        address.is_default = True
        address.save()
        # 将其他地址设置为非默认
        Address.objects.filter(user=request.user).exclude(id=address.id).update(is_default=False)
        return Response({'message': '设置成功'}, status=status.HTTP_200_OK)

# 腾讯云发送短信接口
class OperateTenSms(APIView):
    # 限制访问频率
    throttle_classes = [AnonRateThrottle]
    def post(self, request):
        phone = request.data.get('phone')
        if phone is None:
            return Response({'message': '参数不完整'}, status=status.HTTP_400_BAD_REQUEST)
        # 校验手机号是否合法
        if re.match(r'^1[3-9]\d{9}$', phone) is None:
            return Response({'message': '手机号格式不正确'}, status=status.HTTP_400_BAD_REQUEST)
        # 实例化接口
        code = self.get_random_code()
        time = 5 # 过期时间
        send_sms = SendTenSms(phone, settings.TENCENT_SMS_TEMPLATE_ID, [code, time])
        result = send_sms.send_sms_single()
        if result['result'] == 0:
            # 保存验证码
            obj = VerifyCode.objects.create(code=code, mobile=phone)
            return Response({'message': '发送成功', 'codeId': obj.id, 'codeStatus': result['result']}, status=status.HTTP_200_OK)
        else:
            return Response({'message': send_sms.send_sms_single()['errmsg']}, status=status.HTTP_400_BAD_REQUEST)

    def get_random_code(self):
        code = random.randrange(1000, 999999)
        return code

# 邮箱发送接口
class OperateEmail(APIView):
    # 限制访问频率
    throttle_classes = [AnonRateThrottle]
    def post(self, request):
        email = request.data.get('email')
        # 校验邮箱是否合法
        if re.match(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$', email) is None:
            return Response({'message': '邮箱格式不正确'}, status=status.HTTP_400_BAD_REQUEST)
        code = self.get_random_code()
        time = 5  # 过期时间
        # 把code和time渲染到html模板中，然后发送邮件
        subject = '验证码'
        html_message = render_to_string('email_verif_code.html', {
            'verification_code': code,
            'expiration_time': time,
        })
        from_email = 'max@tabz.work'
        recipient_list = [email]
        if send_email(subject, '', from_email, recipient_list,html_message=html_message):
            # 保存验证码
            obj = VerifyCode.objects.create(code=code, mobile=email)
            return Response({'message': '发送成功', 'codeId': obj.id}, status=status.HTTP_200_OK)
        else:
            return Response({'message': '发送失败'}, status=status.HTTP_400_BAD_REQUEST)
    def get_random_code(self):
        code = random.randrange(1000, 999999)
        return code

# mini_getUserInfo
class MiniWechatLogin(APIView):
    def post(self, request):
        from common.utils import GetAppConfig
        app_config_instance = GetAppConfig()
        wechat_config = app_config_instance.get_wechat_config()
        appid = wechat_config.wechat_app_appid
        appsecret = wechat_config.wechat_app_appsecret
        jscode2session_url = "https://api.weixin.qq.com/sns/jscode2session"
        code = request.data.get('code')
        nickName = request.data.get('nickName')
        avatarUrl = request.data.get('avatar')
        if code is None:
            return Response({'message': '参数不完整'}, status=status.HTTP_400_BAD_REQUEST)
        # 获取openid
        url = f"{jscode2session_url}?appid={appid}&secret={appsecret}&js_code={code}&grant_type=authorization_code"
        # 向微信服务器发起get请求
        response = requests.get(url)
        try:
            # 这里就是拿到的openid和session_key
            openid = response.json()['openid']
            session_key = response.json()['session_key']    # session_key是用来解密用户信息的
        except KeyError:
            errcode = response.json()['errcode']
            errmsg = response.json()['errmsg']
            return Response({'message': errmsg, 'errcode': errcode}, status=status.HTTP_400_BAD_REQUEST)
        else:
            # 主代码块执行完执行到这里，获取或保存用户
            # 判断用户是否存在
            if User.objects.filter(openid=openid).exists():
                user = User.objects.get(openid=openid)
            else:
                # 查询username是否等于nickName
                if User.objects.filter(username=nickName).exists():
                    # 生成一个随机数，作为文件名的一部分
                    random_number = random.randint(1000, 9999)
                    # 组合文件名
                    file_name = f"{nickName}_{random_number}"
                    # 保存用户
                    user = User.objects.create_user(username=file_name, openid=openid, avatar=avatarUrl, user_type=0)
                else:
                    # 保存用户
                    user = User.objects.create_user(username=nickName, openid=openid, avatar=avatarUrl, user_type=0)
        # 生成token
        from rest_framework_simplejwt.tokens import RefreshToken
        refresh = RefreshToken.for_user(user)
        data = {
            'message': '登录成功',
            'data': {
                'token': str(refresh.access_token),
                'refresh': str(refresh),
            }
        }
        return Response(data, status=status.HTTP_200_OK)
    # 通过code快速登录，不需要创建用户，只需要返回token
    def get(self, request):
        from common.utils import GetAppConfig
        app_config_instance = GetAppConfig()
        wechat_config = app_config_instance.get_wechat_config()
        appid = wechat_config.wechat_app_appid
        appsecret = wechat_config.wechat_app_appsecret
        jscode2session_url = "https://api.weixin.qq.com/sns/jscode2session"
        code = request.query_params.get('code')
        if code is None:
            return Response({'message': '参数不完整'}, status=status.HTTP_400_BAD_REQUEST)
        # 获取openid
        url = f"{jscode2session_url}?appid={appid}&secret={appsecret}&js_code={code}&grant_type=authorization_code"
        # 向微信服务器发起get请求
        response = requests.get(url)
        try:
            # 这里就是拿到的openid和session_key
            openid = response.json()['openid']
            session_key = response.json()['session_key']    # session_key是用来解密用户信息的
        except KeyError:
            errcode = response.json()['errcode']
            errmsg = response.json()['errmsg']
            return Response({'message': errmsg, 'errcode': errcode}, status=status.HTTP_400_BAD_REQUEST)
        else:
            # 主代码块执行完执行到这里，获取或保存用户
            # 判断用户是否存在
            if User.objects.filter(openid=openid).exists():
                user = User.objects.get(openid=openid)
            else:
                return Response({'message': '用户不存在'}, status=status.HTTP_400_BAD_REQUEST)
        # 生成token
        from rest_framework_simplejwt.tokens import RefreshToken
        refresh = RefreshToken.for_user(user)
        data = {
            'message': '登录成功',
            'data': {
                'token': str(refresh.access_token),
                'refresh': str(refresh),
            }
        }
        return Response(data, status=status.HTTP_200_OK)

# 讯飞接口
class OperateXunFei(APIView):
    text = []

    def get_text(self, role, content):
        jsoncon = {'role': role, 'content': content}
        self.text.append(jsoncon)
        return self.text

    def getlength(self, text):
        length = 0
        for content in text:
            temp = content["content"]
            leng = len(temp)
            length += leng
        return length
    def checklen(self, text):
        while (self.getlength(text) > 8000):
            del text[0]
        return text

    def post(self, request):
        questionFlag = request.data.get('question')
        if questionFlag is None or questionFlag == "":
            return Response({'message': '参数不完整'}, status=status.HTTP_400_BAD_REQUEST)
        question = self.checklen(self.get_text('user', questionFlag))
        SparkApi.answer = ""
        SparkApi.main(question)
        self.get_text('assistant', SparkApi.answer)
        return Response({'message': '获取成功', 'answer': SparkApi.answer}, status=status.HTTP_200_OK)