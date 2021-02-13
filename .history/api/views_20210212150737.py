from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
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
            pass
        return Response({"code": 400, "status": "failure", "message": "Empty Field", "details": serializer.errors})

# return Response({"code": 200, "status": "success", "message": "User Account Created", "details": dict})
# return Response({"code": 400, "status": "failure", "message": "Empty Field", "details": serializer.errors})

