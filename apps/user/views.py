import re

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.user.models import User

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
        result['token'] = result.pop('access')  # 将access改为token
        result['user_id'] = serializer.user.id
        result['username'] = serializer.user.username
        result['email'] = serializer.user.email
        result['mobile'] = serializer.user.mobile
        result['money'] = serializer.user.money
        result['integral'] = serializer.user.integral


        return Response(serializer.validated_data, status=status.HTTP_200_OK)

# 注册
class RegisterView(APIView):
    def post(self, request):
        # 获取参数
        data = request.data
        username = data.get('username')
        password = data.get('password')
        password_confirm = data.get('password_confirm')
        email = data.get('email')
        if all([username, password, password_confirm, email]) is False:
            return Response({'message': '参数不完整'}, status=status.HTTP_400_BAD_REQUEST)
        if password != password_confirm:
            return Response({'message': '两次密码不一致'}, status=status.HTTP_400_BAD_REQUEST)
        # 校验用户是否存在
        if User.objects.filter(username=username).exists():
            return Response({'message': '用户已存在'}, status=status.HTTP_400_BAD_REQUEST)
        # 校验邮箱格式
        if re.match(r'^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email) is None:
            return Response({'message': '邮箱格式不正确'}, status=status.HTTP_400_BAD_REQUEST)
        # 校验邮箱格式和是否绑定
        if User.objects.filter(email=email).exists():
            return Response({'message': '邮箱已绑定'}, status=status.HTTP_400_BAD_REQUEST)
        # 保存用户
        user = User.objects.create_user(username=username, password=password, email=email)
        # 返回用户信息
        return Response({
            'id': user.id,
            'username': user.username,
            'email': user.email,
        }, status=status.HTTP_201_CREATED)