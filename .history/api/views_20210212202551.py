from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.http import Http404, HttpResponse, JsonResponse
from .models import User,UserProfile
from django.contrib.auth import authenticate, login, logout
from rest_framework.authentication import SessionAuthentication, BasicAuthentication 

from .serializers import RegisterSerializer, LoginSerializer

def OTPGen():
    string = '123456789'
    OTP = ""
    varlen = len(string)
    for i in range(6):
        OTP += string[m.floor(random.random() * varlen)]
    return OTP


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return


class RegisterAPIView(APIView):
    # authentication_classes = (
    #     CsrfExemptSessionAuthentication,
    #     BasicAuthentication)

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.data['username']
            password = serializer.data['password']
            confirm_password = serializer.data['confirm_password']

            user = User.objects.filter(username=username)
            if not user.exists():
                if not password == confirm_password:
                    return Response({"code": 400, "status": "failure",
                            "message": "Password Doesnot Matched",
                            "details": serializer.errors})
                User.objects.create(username=username,
                                    password=password)
                return JsonResponse({"code": 200, "status": "success",
                                "message": "User Account Created",
                                "details": serializer.data})
                
            return JsonResponse({"code": 400, "status": "Failure",
                                "message": "User Already Exist",
                                "details": []})
        return JsonResponse({"code": 400, "status": "failure",
                        "message": "Empty Field",
                        "details": serializer.errors})


class LoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        # serializer = LoginSerializer(data=request.data)
        # if serializer.is_valid():
        print(request.queryparams.data)
        username = request.queryparams.get('username')
        password = request.queryparams.get['password']
        try:
            query = User.objects.get(username=username, password=password)
            print(query,'as')
        except User.DoesNotExist as e:
            print(e)
            return JsonResponse({"code": 400, "status": "failure",
                        "message": "Invalid Credentials",
                        "details": 'Invalid Credentails'})

        token, create = Token.objects.get_or_create(user_id=query.id)
        toret = {}
        toret['username'] = username
        toret['token'] = token.key
        return JsonResponse({"code": 200, "status": "success", "message": "User Logged In", "details": toret})
        # return JsonResponse({"code": 400, "status": "failure",
        #                  "message": "Empty Field",
        #                  "details": serializer.errors})

class UserAdditionalDataAddAPIView(APIView):

    def post(self, request, *args, **kwargs):
        try:
            token = request.META['HTTP_AUTHORIZATION']
        except:
            return Response({'code': 400, 'status': 'failure', 'message': 'User Token Not Provided'})
        try:
            token = (token.split("er")[1])
        except:
            return Response({'code': 400, 'status': 'failure', 'message': 'No Token Keyword Provided'})
        try:
            usid = Token.objects.get(key=token)
        except:
            return Response({'code': 404, 'status': 'failure', 'message': 'Invalid Credentials'})
        user_id = usid.user_id
        
        