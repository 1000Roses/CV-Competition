from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import serializers, viewsets, permissions
from django.contrib.auth import authenticate
from .serializers import SignupSerializer, LoginSerializer
from .models import CustomUser


class UserViewSet(viewsets.ViewSet):
    
    @action(detail= False, methods= ['post'])
    def login(self, request):
        email = request.data.get('email', None)
        password= request.data.get('password', None)
        
        user = authenticate(username= email, password= password)

        if user:
            serializer = LoginSerializer(user)
            return Response(serializer.data)
        return Response({ 'error': 'wrong password or username' })
    

    @action(detail= False, methods = ['post'])
    def signup(self, request):
        try:
            is_phone_exist = CustomUser.objects.get(phone=request.data['phone'])
            return Response({ 'error': 'phone is already used' })
        except:
            pass

        try:
            is_email_exist = CustomUser.objects.get(email=request.data['email'])
            return Response({ 'error': 'email is already used' })
        except:
            pass

        
    
        serializer = SignupSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
                
        return Response({ 'error': 'invalid field' })
