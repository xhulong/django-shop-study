# 返回一个html页面
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
