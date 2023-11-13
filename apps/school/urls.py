from django.urls import path
from .views import SchoolViewSet

urlpatterns = [
    path('list/', SchoolViewSet.as_view({'get': 'list'})),
]
