import re
import random

from django.conf import settings
from django.shortcuts import render
from rest_framework import status, mixins
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.user.models import User, Address, VerifyCode
from apps.user.serializer import UserSerializer, AddressSerializer
from common.permissions import IsAddressPermissions,IsOwnerOrReadOnly
from common.tencent_sms import SendTenSms
from common.utils import send_email,random_username


# Create your views here.

# 重写登录方法
class LoginView(TokenObtainPairView):
    def post(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        result = serializer.validated_data
        userInfo = {
            'user_id': serializer.user.id,
            'username': serializer.user.username,
            'email': serializer.user.email,
            'mobile': serializer.user.mobile,
            'money': serializer.user.money,
            'integral': serializer.user.integral,
            'avatar': serializer.user.avatar,
        }
        data = {
            'message': '登录成功',
            'data': {
                'userInfo': userInfo,
                'token': result['access'],
                'refresh': result['refresh'],
            }
        }


        return Response(data, status=status.HTTP_200_OK)
    #修改密码
    def put(self, request, *args, **kwargs):
        # 获取参数
        data = request.data
        phone = data.get('phone')
        password = data.get('password')
        code = data.get('code')
        print(phone,password,code)
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

        user = User.objects.create_user(username=random_username(), password=password,mobile=username)
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

    # 上传头像
    def upload_avatar(self, request, *args, **kwargs):
        obj = self.get_object()
        avatar = request.data.get('avatar')
        if avatar is None:
            return Response({'message': '参数不完整'}, status=status.HTTP_400_BAD_REQUEST)
        size = avatar.size
        if size > 1024 * 1024 * 2:
            return Response({'message': '图片过大'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(obj, data={'avatar': avatar}, partial=True)
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save()
            # 数据保存成功，可以执行其他操作
        except Exception as e:
            print(e)
            return Response({'message': '上传失败'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': '上传成功', 'avatar': serializer.data['avatar']}, status=status.HTTP_200_OK)

    # 绑定手机
    def bind_mobile(self, request, *args, **kwargs):
        mobile = request.data.get('mobile')
        code = request.data.get('code')
        codeId = request.data.get('codeId')
        # 校验验证码
        result = self.verif_code(mobile, codeId, code)
        if result is not None:
            return result
        # 保存用户
        if User.objects.filter(mobile=mobile).exists():
            return Response({'message': '手机号已绑定'}, status=status.HTTP_400_BAD_REQUEST)
        # 判断用户是否已绑定
        obj = request.user
        print(obj.mobile)
        if obj.mobile is not None and obj.mobile != "":
            return Response({'message': '用户已绑定'}, status=status.HTTP_400_BAD_REQUEST)
        obj.mobile = mobile
        obj.save()
        # 删除验证码
        VerifyCode.objects.filter(id=codeId).delete()
        return Response({'message': '绑定成功'}, status=status.HTTP_200_OK)

    # 解绑手机
    def unbind_mobile(self, request, *args, **kwargs):
        mobile = request.data.get('mobile')
        code = request.data.get('code')
        codeId = request.data.get('codeId')
        # 校验验证码
        result = self.verif_code(mobile, codeId, code)
        if result is not None:
            return result
        # 解绑手机（验证手机已绑定手机号）
        obj = request.user
        if obj.mobile != mobile:
            return Response({'message': '手机号不正确'}, status=status.HTTP_400_BAD_REQUEST)
        obj.mobile = ""
        obj.save()
        # 删除验证码
        VerifyCode.objects.filter(id=codeId).delete()
        return Response({'message': '解绑成功'}, status=status.HTTP_200_OK)

    # 修改用户昵称
    def update_last_name(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        last_name = request.data.get('last_name')
        if last_name is None or last_name == "":
            return Response({'message': '参数不完整'}, status=status.HTTP_400_BAD_REQUEST)
        obj = request.user
        obj.last_name = last_name
        obj.save()
        return Response({'message': '修改成功'}, status=status.HTTP_200_OK)



    # 封装验证码
    @staticmethod
    def verif_code(mobile, codeId, code):
        if not all([mobile, codeId, code]):
            return Response({'message': '参数不完整'}, status=status.HTTP_400_BAD_REQUEST)
        # 校验手机号是否合法
        if re.match(r'^1[3-9]\d{9}$', mobile) is None:
            return Response({'message': '手机号格式不正确'}, status=status.HTTP_400_BAD_REQUEST)
        # 校验验证码 通过返回none，不通过返回对象
        try:
            verify_code = VerifyCode.objects.get(id=codeId, mobile=mobile, code=code)
            # 校验验证码是否过期
            if verify_code.is_expired(expiration_minutes=5):
                return Response({'message': '验证码过期'}, status=status.HTTP_400_BAD_REQUEST)
        except VerifyCode.DoesNotExist:
            return Response({'message': '验证码错误'}, status=status.HTTP_400_BAD_REQUEST)
        return None





# 文件访问
class FileView(APIView):
    def get(self, request, filename):
        from django.conf import settings
        from django.http import FileResponse
        import os
        path = os.path.join(settings.MEDIA_ROOT, filename)
        if os.path.exists(path) is False:
            return Response({'message': '文件不存在'}, status=status.HTTP_404_NOT_FOUND)
        return FileResponse(open(path, 'rb'))

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
        subject = 'Hello, this is the subject'
        message = 'This is the email message.'
        from_email = 'max@tabz.work'
        recipient_list = ['927266886@qq.com']
        print(111)
        if send_email(subject, message, from_email, recipient_list):
            return render(request, 'success_template.html', {'message': 'Email sent successfully!'})
        else:
            return render(request, 'error_template.html', {'message': 'Email sending failed!'})

# 微信小程序登录
# class WechatLogin(APIView):
#     def post(self, request):
#         data = request.data
#         code = data.get('code')
#         if code is None:
#             return Response({'message': '参数不完整'}, status=status.HTTP_400_BAD_REQUEST)
#         # 获取openid
#         from common.wechat import WeChat
#         wechat = WeChat()
#         openid = wechat.get_openid(code)
#         if openid is None:
#             return Response({'message': '登录失败'}, status=status.HTTP_400_BAD_REQUEST)
#         # 判断用户是否存在
#         if User.objects.filter(username=openid).exists():
#             user = User.objects.get(username=openid)
#         else:
#             user = User.objects.create_user(username=openid, password=openid)
#         # 生成token
#         from rest_framework_simplejwt.tokens import RefreshToken
#         refresh = RefreshToken.for_user(user)
#         return Response({
#             'token': str(refresh.access_token),
#             'user_id': user.id,
#             'username': user.username,
#             'email': user.email,
#         }, status=status.HTTP_200_OK)


# class WechatLogin(APIView):
#
#     """ 获取opeid存储用户信息"""
#
#     appid = 'wxxxxxxxx'
#     appsecret = ''
#     jscode2session_url = "https://api.weixin.qq.com/sns/jscode2session"
#
#     def post(self, request, format=None):
#         # 获取到前端回传过来的code
#         code = json.loads(request.body).get('code')  # 这个code有效期为5分钟
#         # 构造向wx发送请求的url
#         url = f"{self.jscode2session_url}?appid={self.appid}&secret={self.appsecret}&js_code={code}&grant_type=authorization_code"
#         # 向微信服务器发起get请求
#         response = requests.get(url)
#         try:
#             # 这里就是拿到的openid和session_key
#             openid = response.json()['openid']
#             session_key = response.json()['session_key']
#         except KeyError:
#             return Response({'code': 'fail'})
#         else:
#             # 主代码块执行完执行到这里，获取或保存用户
#             user, iscreated = User.objects.get_or_create(
#                 username=openid,
#                 password=openid,
#                 defaults={'username': openid}
#             )
#
#             # 采用JWT登录的话，这里就返回token信息
#             from foodapi.utils import get_tokens_for_user
#             token_dict = get_tokens_for_user(user)
#             try:
#                 userinfo = user.userinfo
#             except UserInfo.DoesNotExist:
#                 userinfo, isupdated = UserInfo.objects.update_or_create(owner=user, name=openid, defaults={'owner': user})
#             avatar = f"http://{request.get_host()}/{str(userinfo.avatar)}"
#             return Response({"code": "success", "openid": openid, "name": userinfo.name, "avatar": avatar, **token_dict}, status=status.HTTP_200_OK)

