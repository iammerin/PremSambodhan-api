from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout

from .serializers import *

def OTPGen():
    string = '123456789'
    OTP = ""
    varlen = len(string)
    for i in range(6):
        OTP += string[m.floor(random.random() * varlen)]
    return OTP


class RegisterAPIView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.data['username']
            password = serializer.data['password']
            confirm_password = serializer.data['confirm_password']

            if not password == confirm_password:
                
                return Response({"code": 400, "status": "failure",
                         "message": "Password Doesnot Matched",
                         "details": serializer.errors})
                
            User.objects.create(username=username,
                                password=password)
            
            return Response({"code": 200, "status": "success",
                             "message": "User Account Created",
                             "details": serializer.data})
            
        return Response({"code": 400, "status": "failure",
                         "message": "Empty Field",
                         "details": serializer.errors})

# return Response({"code": 200, "status": "success", "message": "User Account Created", "details": dict})
# return Response({"code": 400, "status": "failure", "message": "Empty Field", "details": serializer.errors})

class LoginAPIView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.data['username']
            password = serializer.data['password']
            user = authenticate(
                    mobile_number=username, password=password)
            if user is None:
                
        return Response({"code": 400, "status": "failure",
                         "message": "Empty Field",
                         "details": serializer.errors})