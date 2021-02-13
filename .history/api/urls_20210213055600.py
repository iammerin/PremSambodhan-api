from django.urls import path,include
from .views import RegisterAPIView, LoginAPIView,, UpdateProfileAPIView, UserAdditionalDataAddAPIView, MessageAPIView, MessagingAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('add/additionaldata/', UserAdditionalDataAddAPIView.as_view()),
    path('get/additionaldata/', GetProfileAPIView.as_view()),
    path('update/additionaldata/', UpdateProfileAPIView.as_view()),
    path('message/', MessagingAPIView.as_view()),
]