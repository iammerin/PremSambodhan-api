from django.urls import path,include
from .views import RegisterAPIView, LoginAPIView, UserAdditionalDataAddAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('add/additionaldata/', UserAdditionalDataAddAPIView.as_view()),
]