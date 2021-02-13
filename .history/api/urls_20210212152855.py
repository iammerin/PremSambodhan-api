from django.urls import path,include
from .views import RegisterAPIViews, LoginAPIViews

urlpatterns = [
    path('register/', RegisterAPIView),
]