from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.http import Http404, HttpResponse, JsonResponse
from .models import User,UserProfile, Message
from django.contrib.auth import authenticate, login, logout
from rest_framework.authentication import SessionAuthentication, BasicAuthentication 

from .serializers import RegisterSerializer, LoginSerializer, UserDataSerializer, MessageSerializer, MessagingSerializer

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
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.data['username']
            print(username)
            password = serializer.data['password']
            if username is None:
                return JsonResponse({"code": 400, "status": "failure",
                            "message": "Must Have Username"})
            else:
                pass

            if password is None:
                return JsonResponse({"code": 400, "status": "failure",
                            "message": "Must Have Password"})
            try:
                query = User.objects.get(username=username, password=password)
                print(query,'as')
            except User.DoesNotExist:
                return JsonResponse({"code": 400, "status": "failure",
                            "message": "Invalid Credentials",
                            "details": 'Invalid Credentails'})

            token, create = Token.objects.get_or_create(user_id=query.id)
            toret = {}
            toret['username'] = username
            toret['token'] = token.key
            return JsonResponse({"code": 200, "status": "success", "message": "User Logged In", "details": toret})
        return JsonResponse({"code": 400, "status": "failure",
                         "message": "Empty Field",
                         "details": serializer.errors})


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
        serializer = UserDataSerializer(data=request.data)
        if serializer.is_valid():
            queryset = UserProfile.objects.filter(user_id=user_id)
            if queryset is not None:
                
                return JsonResponse({"code": 400, "status": "Failure",
                                "message": "Data already added",
                                "details":{}})
            serializer.save(user_id=user_id)

            return JsonResponse({"code": 200, "status": "success",
                                "message": "User Data Created",
                                "details": serializer.data})
            
        return JsonResponse({"code": 400, "status": "failure",
                            "message": "Empty Field",
                             "details": serializer.errors})
        


class MessageAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return JsonResponse({"code": 200, "status": "success",
                                "message": "Successfully Sent",
                                "details": serializer.data})

        return JsonResponse({"code": 400, "status": "failure",
                            "message": "Empty Field",
                             "details": serializer.errors})
        
    def get(self, request, sender=None, receiver=None):
        messages = Message.objects.filter(
            sender_id=sender, receiver_id=receiver
            )
        serializer = MessageSerializer(
            messages, many=True, context={'request': request}
            )
        return JsonResponse(serializer.data, safe=False)


class MessagingAPIView(APIView):
    def get(self, request):
        user = User.objects.all().values('id','username')
        toret = {}
        for each in user:
            toret['id'] = each['user__id']
            toret['username'] = each['user__username']
            toret['image'] = each['profile_image']
            
        return JsonResponse({"code": 200, "status": "success",
                                "message": "Successfully Fetched",
                                "details": toret})


class CreateStory(APIView):
    pass