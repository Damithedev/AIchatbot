from django.db import transaction
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.exceptions import APIException, AuthenticationFailed, NotAcceptable
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User, Chat
from .serializers import UserSerializer, ChatSerializer
import jwt, datetime
from .aiapi import dummy_chatbot_response


#Register User
class Registeruser(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        username = request.data.get('username')
        user = User.objects.filter(username=username).first()
        if user:
            raise NotAcceptable(detail='Username already exists')
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#List User
class ListUsers(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



#Login User
class Loginview(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.filter(username=username).first()
        if user is None:
            raise AuthenticationFailed('User not found')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password')
        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow(),
        }
        token = jwt.encode(payload, 'secret', algorithm='HS256')
        return Response({
            'token': token,
        }, status=status.HTTP_200_OK)

#Send Message Endpoints
class SendMessage(APIView):

    def post(self, request):
        message = request.data.get('message')
        user = request.user
        print(request)
        with transaction.atomic():
            if user.tokens < 100:
                raise AuthenticationFailed('Not enough tokens')
            user.tokens -= 100
            user.save()

        # Perform async response handling
        response = dummy_chatbot_response(message)

        # Serialize and save the chat message
        serializer = ChatSerializer(data={
            'message': message,
            'user': user.id,
            'response': response
        })

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data.get('response'), status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Check Authenticated User Token
class Checktoken(APIView):
    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)

        return Response(serializer.data.get('tokens'), status=status.HTTP_200_OK)
