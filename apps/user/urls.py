from django.contrib import admin
from django.urls import path
from apps.user.views import LoginView,RegisterView

urlpatterns = [
    path('login/', LoginView.as_view(), name='token_obtain_pair'),
    path('register/', RegisterView.as_view(), name='token_obtain_pair'),
]
