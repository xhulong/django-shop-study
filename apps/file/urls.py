from django.urls import path

from .views import FileDetailAPIView, FileListCreateAPIView

urlpatterns = [
    # 文章文件URL
    path('files/', FileListCreateAPIView.as_view()),
    path('filesDetail/<int:pk>/', FileDetailAPIView.as_view())
    ]