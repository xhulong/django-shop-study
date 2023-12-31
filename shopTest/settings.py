"""
Django settings for shopTest project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from datetime import timedelta
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-gz6le$+9%zan+7w=qay@_3ju*p=t_r)ul1#1_^d7%9myfn1j#8'
SIMPLEUI_HOME_INFO = False  # 关闭首页信息
SIMPLEUI_ANALYSIS = False   # 关闭统计
SIMPLEUI_HOME_PAGE = None   # 关闭首页

DEBUG = False

ALLOWED_HOSTS = [
    '*'
]
CSRF_TRUSTED_ORIGINS = ["https://admin.tabz.work"]

# Application definition

INSTALLED_APPS = [
    # 'daphne',
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',  # 支持跨域请求
    'rest_framework',
    'rest_framework_simplejwt',
    'ckeditor',  # 富文本编辑器
    'django_filters',  # 过滤器
    'solo',  # 单例模型
    'channels',
    'apps.user',
    'apps.global_system',
    'apps.school',
    'apps.good',
    'apps.activity',
    'apps.demand',
    'apps.order',
    'apps.article',
    'apps.file',
    'apps.student_manage',
    'apps.book_manage',
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # 支持跨域请求
]

ROOT_URLCONF = 'shopTest.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'shopTest.wsgi.application'
ASGI_APPLICATION = 'shopTest.asgi.application'  # 新增
# daphne shopTest.asgi:application --port 8001 --bind
# 设置通道层的通信后台 - 本地测试用
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    }
}
SIMPLEUI_LOGO = 'https://qiniu.tabz.work//picGo/乒乓球拍.png'
# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "tabzxiaohu",
        'USER': 'tabzxiaohu',
        'PASSWORD': 'tabzxiaohu',
        'HOST': 'db',
        'PORT': '3306',
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': "web_shop",
#         'USER': 'root',
#         'PASSWORD': '123123',
#         'HOST': 'localhost',
#         'PORT': '3306',
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# settings.py

STATIC_URL = '/static/'

# 这是 Django 收集所有静态文件的地方
STATIC_ROOT = os.path.join(BASE_DIR, 'collect_static')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ORIGIN_ALLOW_ALL = True  # 允许跨域请求

# 自定义用户模型类
AUTH_USER_MODEL = 'user.User'

# 配置drf的认证类
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    # 指定用于支持coreapi的Schema
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    # 指定过滤器
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.OrderingFilter'
    ],
    'DEFAULT_RENDERER_CLASSES': ['rest_framework.renderers.JSONRenderer'],
    # 限流 一分钟只能访问三次
    # 'DEFAULT_THROTTLE_CLASSES': [
    #     'rest_framework.throttling.AnonRateThrottle',
    #     'rest_framework.throttling.UserRateThrottle'
    # ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '1/min',
        'user': '1/min'
    }
}
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),  # token有效期
    'REFRESH_TOKEN_LIFETIME': timedelta(days=14),  # 刷新token有效期
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': True,
    'ALGORITHM': 'HS256',  # 加密算法
    'SIGNING_KEY': SECRET_KEY,  # 签名密钥
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,

    "AUTH_HEADER_TYPES": ('Bearer',),
    'USER_ID_FIELD': 'id',
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    'USER_ID_CLAIM': 'user_id',
}

AUTHENTICATION_BACKENDS = [  # 自定义用户登录认证，实现多字段登录
    'common.authenticate.CustomBackend'
]

# 文件上传的保存路径
MEDIA_ROOT = BASE_DIR / 'files'

# 文件上传的访问路径
MEDIA_URL = '/files/'

TENCENT_SMS_APP_ID = '1400740456'
TENCENT_SMS_APP_KEY = '1d2f79486e383269a90e4151c41f869a'
TENCENT_SMS_SIGN = '小O校园公众号'
TENCENT_SMS_TEMPLATE_ID = 1566290

# 邮件配置
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.ym.163.com'
EMAIL_PORT = 465  # 通常是 587 或 465
EMAIL_USE_SSL = True  # 使用 TLS 加密 (或使用 EMAIL_USE_SSL = True 如果需要 SSL 加密)
EMAIL_HOST_USER = 'max@tabz.work'
EMAIL_HOST_PASSWORD = 'LIpaoxiao0829'
DEFAULT_FROM_EMAIL = 'max@tabz.work'
