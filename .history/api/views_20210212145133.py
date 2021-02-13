from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

def OTPGen():
    string = '123456789'
    OTP = ""
    varlen = len(string)
    for i in range(6):
        OTP += string[m.floor(random.random() * varlen)]
    return OTP
